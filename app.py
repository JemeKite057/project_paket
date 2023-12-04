import streamlit as st
from sqlalchemy import text

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://akmalabidin004:sPK78YJDilom@ep-damp-pine-78588298.ap-southeast-1.aws.neon.tech/neondb")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS pesanan (id serial, nama_penerima varchar, nama_pengirim varchar, alamat_penerima varchar, \
                                                       alamat_pengirim varchar, berat varchar, kode_pos varchar, nomor_resi varchar, tanggal date);')
    session.execute(query)

st.header('tes 2')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM pesanan ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO pesanan (nama_penerima, nama_pengirim, alamat_penerima, alamat_pengirim, berat, kode_pos ,nomor_resi , tanggal) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':None})
            session.commit()

    data = conn.query('SELECT * FROM pesanan ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        nama_penerima_lama = result["nama_penerima"]
        nama_pengirim_lama = result["nama_pengirim"]
        alamat_penerima_lama = result["alamat_penerima"]
        alamat_pengirim_lama = result["alamat_pengirim"]
        berat_lama = result["berat"]
        kode_pos_lama = result["kode_pos"]
        nomor_resi_lama = result["nomor_resi"]
        tanggal_lama = result["tanggal"]

        with st.expander(f'a.n. {nama_pengirim_lama}'):
            with st.form(f'data-{id}'):
                nama_penerima_baru = st.text_input("nama_penerima", nama_penerima_lama)
                nama_pengirim_baru = st.text_input("nama_pengirim", nama_pengirim_lama)
                alamat_penerima_baru = st.text_input("alamat_penerima", alamat_penerima_lama)
                alamat_pengirim_baru = st.text_input("alamat_pengirim", alamat_pengirim_lama)
                berat_baru = st.text_input("berat", berat_lama)
                kode_pos_baru = st.text_input("kode_pos", kode_pos_lama)
                nomor_resi_baru = st.text_input("nomor_resi", waktu_lama)
                tanggal_baru = st.date_input("tanggal", tanggal_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE pesanan \
                                          SET nama_penerima=:1, nama_pengirim=:2, alamat_penerima=:3, alamat_pengirim=:4, \
                                          berat=:5, kode_pos=:6, nomor_res=:7, tanggal=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':nama_penerima_baru, '2':nama_pengirim_baru, '3':alamat_penerima_baru, '4':alamat_pengirim_baru, 
                                                    '5':berat_baru, '6':kode_pos_baru, '7':nomor_resi_baru, '8':tanggal_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM pesanan WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()