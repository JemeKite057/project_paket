drop table if exists pesanan;
create table pesanan (
	id serial,
	nama_penerima text,
	nama_pengirim text,
	alamat_penerima text,
	alamat_pengirim text,
	berat text,
	kode_pos text,
	nomor_resi text,
	tanggal date
);

insert into pesanan (nama_penerima, nama_pengirim, alamat_penerima, alamat_pengirim, berat, kode_pos, nomor_resi, tanggal) 
values
	('Akmal', 'Lampu Nyala', 'Surabaya', 'Bandung', 1000, 30604, 10000, '2023-10-01'),
	('Desta', 'Skincare Cantik', 'Palembang', 'Jakarta', 250, 20402, 20000988, '2022-10-02'),
	('Dinda', 'Kimia Bahan', 'Palembang', 'Semarang', 3000, 20403, 2000097, '2022-10-03'),
	('Gus', 'Walter Putih', 'Alberqurque', 'New Mexico', 400000, 20056, 200098, '2022-10-04'),
	('Betmen', 'Badut Joker', 'Gotham', 'Metropolis', 2300, 30432 , 2009832, '2022-10-05'),
	('Jawir', 'Ireng Paketan', 'Tulungagung', 'Jember', 3000, 20430, 2000890, '2022-10-06'),
	('Anggi', 'Paket lah', 'Surabaya', 'Palembang', 8888, 20120, 103000, '2022-10-07'),
	('Spidermen', 'Bom Goblin', 'New York', 'Goblin Tower', 12000, 20102, 2010000, '2022-10-08'),
	('Alya', 'Paketan', 'Sidoarjo', 'Surabaya', 10000, 99999, 2010092, '2022-10-09'),
	('Apnan', 'Apa aja', 'Jombang', 'Surabaya', 62838, 20000, 29900,'2022-11-10')