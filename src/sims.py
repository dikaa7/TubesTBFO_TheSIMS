# Nama File : sims.py
# Tanggal: 19 September 2019
# Topik: Tubes TBFO
# Programmer : 
# Ade Surya Handika	- 13518007
# Muhammad Rikzi Ismail - 13518148
import constant as c

class Status:
	def __init__(self, h, e, f):
		# Konstruktor dengan input hygiene, energy, dan fun
		'''Defines  variables'''
		self.hygiene = h
		self.energy = e
		self.fun = f	

	def Start(self):
		# Mengembalikan nilai status ke kondisi Start
		self.hygiene = 0
		self.energy = 10
		self.fun = 0
	
	''' SELEKTOR '''
	def AddHygiene(self,h):
		# Menambah nilai hygiene sebesar h
		self.hygiene += (h)
	
	def AddEnergy(self,e):
		# Menambah nilai energy sebesar e
		self.energy += (e)
		
	def AddFun(self,f):
		# Menambah nilai fun sebesar f
		self.fun += (f)
	
	''' INPUT/OUTPUT '''
	def TulisStatus(self):
		# Menulis status the sims
		print("===============STATUS===============")
		print("Hygiene	= " + str(self.hygiene))
		print("Energy	= " + str(self.energy))
		print("Fun	= " + str(self.fun))
	
	def BacaStatus(self):
		# Mengubah nilai status
		# Membaca nilai status sampai kondisi valid (0 <= status <= 15)
		
		print("===========BACA STATUS==============")
		
		self.hygiene = int(input("# Masukkan nilai Hygiene   : "))
		while (not(self.IsHygieneValid())):
			print("Nilai Hygiene tidak Valid")
			self.hygiene = int(input("# Masukkan nilai Hygiene   : "))
		
		self.energy = int(input("# Masukkan nilai Energy    : "))
		while (not(self.IsEnergyValid())):	
			print("Nilai Energy tidak Valid")
			self.energy = int(input("# Masukkan nilai Energy    : "))
		
		self.fun = int(input("# Masukkan nilai Fun       : "))
		while (not(self.IsFunValid())):
			print("Nilai Fun tidak Valid")
			self.fun = int(input("# Masukkan nilai Fun       : "))
		
		print("Status berhasil diubah menjadi : (" + str(self.hygiene) + "," + str(self.energy) + "," + str(self.fun) + ")")
	def TulisAksi(self):
		# Menampilkan list aksi yang dapat digunakan
		print("=============LIST AKSI==============")
		print("Ketikkan keyword yang akan dipilih kemudian 'enter', misal: Tidur Siang")
		print("List Keyword Aksi: ")
		print("1. Tidur Siang", end="           "); print("10. Buang Air Besar")
		print("2. Tidur Malam", end="           ");	print("11. Bersosialisasi ke Kafe")
		print("3. Makan Hamburger", end="       "); print("12. Bermain Media Sosial")
		print("4. Makan Pizza", end="           "); print("13. Bermain Komputer")
		print("5. Makan Steak and Beans", end=" "); print("14. Mandi")
		print("6. Minum Air", end="             "); print("15. Cuci Tangan")
		print("7. Minum Kopi", end="            "); print("16. Mendengar Musik di Radio")
		print("8. Minum Jus", end="             "); print("17. Membaca Koran")
		print("9. Buang Air Kecil", end="       "); print("18. Membaca Novel")
		print("99. List Aksi")
	
	def BacaAksi(self):
		# Membaca input aksi sampai user menuliskan 'menu' (kembali ke menu utama)
		# atau sampai kondisi Status (0,0,0) atau (15,15,15) (Permainan berhenti)
		if (not(self.IsDie()) and (not(self.IsFull()))):
			self.TulisStatus()
			self.TulisAksi()
			print("============AKSI THE SIMS===========")
			print("Ketikkan Aksi sesuai Keyword yang diberikan")
			print("Ketik 'Menu' untuk kembali ke menu")		
			Baca = "START"
			while((Baca != "menu") and (not(self.IsFull())) and (not(self.IsDie()))):
				print("================AKSI================")
				Baca = str(input("# Keyword Aksi: "))
				Baca = Baca.lower()
				if(Baca == "tidur siang"):
					self.TidurSiang()
				elif(Baca == "tidur malam"):
					self.TidurMalam()
				elif(Baca == "makan hamburger"):
					self.MakanHamburger()
				elif(Baca == "makan pizza"):
					self.MakanPizza()
				elif(Baca == "makan steak and beans"):
					self.MakanSteakAndBeans()
				elif(Baca == "minum air"):
					self.MinumAir()
				elif(Baca == "minum kopi"):
					self.MinumKopi()
				elif(Baca == "minum jus"):
					self.MinumJus()
				elif(Baca == "buang air kecil"):
					self.BuangAirKecil()
				elif(Baca == "buang air besar"):
					self.BuangAirBesar()
				elif(Baca == "bersosialisasi ke kafe"):
					self.BersosialisasiKeKafe()
				elif(Baca == "bermain media sosial"):
					self.BermainMediaSosial()
				elif(Baca == "bermain komputer"):
					self.BermainKomputer()
				elif(Baca == "mandi"):
					self.Mandi()
				elif(Baca == "cuci tangan"):
					self.CuciTangan()
				elif(Baca == "mendengar musik di radio"):
					self.MendengarMusikDiRadio()
				elif(Baca == "membaca koran"):
					self.MembacaKoran()
				elif(Baca == "membaca novel"):
					self.MembacaNovel()			
				elif(Baca == "list aksi"):
					self.TulisAksi()
				elif(Baca == "menu"): 
					print("KEMBALI KE MENU UTAMA")
				else:
					Baca = "Ilegal"
					print("Aksi Tidak Tersedia")

				if ((Baca != "Ilegal") and (Baca != "menu")):
					self.TulisState()
		
		if (self.IsFull()):
			print("==============WIN GAME==============")
			print(" __       __  ______  __    __  ")
			print("|  \  _  |  \|      \|  \  |  \ ")
			print("| $$ / \ | $$ \$$$$$$| $$\ | $$ ")
			print("| $$/  $\| $$  | $$  | $$$\| $$ ")
			print("| $$  $$$\ $$  | $$  | $$$$\ $$ ")
			print("| $$ $$\$$\$$  | $$  | $$\$$ $$ ")
			print("| $$$$  \$$$$ _| $$_ | $$ \$$$$ ")
			print("| $$$    \$$$|   $$ \| $$  \$$$ ")
			print(" \$$      \$$ \$$$$$$ \$$   \$$ ")
			print("")
			print("SELAMAT KAMU MENCAPAI KONDISI IDEAL!!")
			print("KAMU BERHASIL MEMENANGKAN PERMAINAN")
			print(" . . . kembali ke menu")
		elif (self.IsDie()):
			print("=============LOSE GAME==============")
			print(" __         ______    ______   ________  ")
			print("|  \       /      \  /      \ |        \ ")
			print("| $$      |  $$$$$$\|  $$$$$$\| $$$$$$$$ ")
			print("| $$      | $$  | $$| $$___\$$| $$__     ")
			print("| $$      | $$  | $$ \$$    \ | $$  \    ")
			print("| $$      | $$  | $$ _\$$$$$$\| $$$$$    ")
			print("| $$_____ | $$__/ $$|  \__| $$| $$_____  ")
			print("| $$     \ \$$    $$ \$$    $$| $$     \ ")
			print(" \$$$$$$$$  \$$$$$$   \$$$$$$  \$$$$$$$$ ")  
			print("")
			print("STATUS HABIS, KAMU KALAH !!")
			print(" . . . kembali ke menu")		
		else:
			self.BacaMenu()
		
	def TulisMenu(self):
		# Menampilkan list menu program utama
		print("=============LIST MENU==============")
		print("Ketikkan keyword yang akan dipilih kemudian 'enter', misal: Bermain")
		print("List Menu THE SIMS: ")
		print("1. Bermain")
		print("2. Cek Status")
		print("3. Ubah Status")
		print("4. State Awal")
		print("5. Tampilkan Menu")
		print("6. Tampilkan Aksi")
		
	def BacaMenu(self):
		# Membaca input menu untuk program utama sampai user menuliskan 'EXIT'
		self.TulisMenu()
		print("===========MENU THE SIMS============")
		Pilih = str(input("# Keyword Menu: "))
		Pilih = Pilih.lower()
		while (Pilih != "exit"):
			if(Pilih == "bermain"):
				self.BacaAksi()
			elif(Pilih == "cek status"):
				self.TulisStatus()
			elif(Pilih == "ubah status"):
				self.BacaStatus()
			elif(Pilih == "state awal"):
				self.Start()
				print("Mengembalikan nilai status ke state awal (0,10,0)")
			elif(Pilih == "tampilkan menu"):
				self.TulisMenu()
			elif(Pilih == "tampilkan aksi"):
				self.TulisAksi()
			else:
				print("Menu tidak tersedia")
			print("================MENU================")
			Pilih = str(input("# Keyword Menu: "))
			Pilih = Pilih.lower()
			
	def TulisState(self):
		# Menuliskan state menggunakan simbol 0,L,M,H
		print("================STATE===============")
		print("STATE : ", end="")
		if (self.hygiene == 0):
			print('0', end="")
		elif (self.hygiene == 5):
			print('L', end="")
		elif (self.hygiene == 10):
			print('M', end="")
		elif (self.hygiene == 15):
			print('H', end="")
			
		
		if (self.energy == 0):
			print('0', end="")
		elif (self.energy == 5):
			print('L', end="")
		elif (self.energy == 10):
			print('M', end="")
		elif (self.energy == 15):
			print('H', end="")
			
		
		if (self.fun == 0):
			print('0')
		elif (self.fun == 5):
			print('L')
		elif (self.fun == 10):
			print('M')
		elif (self.fun == 15):
			print('H')
	
	''' PREDIKAT '''
	def IsHygieneValid(self):
		# Mengecek nilai hygiene, true (valid) untuk (0 <= Hygiene <= 15)
		return ((self.hygiene >= c.MINHYGIENE) and (self.hygiene <= c.MAXHYGIENE))
	
	def IsEnergyValid(self):
		# Mengecek nilai energy, true (valid) untuk (0 <= Hygiene <= 15)
		return ((self.energy >= c.MINENERGY) and (self.energy <= c.MAXENERGY))
	
	def IsFunValid(self):
		# Mengecek nilai fun, true (valid) untuk (0 <= Hygiene <= 15)
		return ((self.fun >= c.MINFUN) and (self.fun <= c.MAXFUN))
	
	def IsHygieneFull(self):
		# Mengecek apakah nilai hygiene maksimal, true untuk Hygiene => 15;
		return (self.hygiene >= c.MAXHYGIENE)
	
	def IsEnergyFull(self):
		# Mengecek apakah nilai energy maksimal, true untuk energy => 15;
		return (self.energy >= c.MAXENERGY)
	
	def IsFunFull(self):
		# Mengecek apakah nilai fun maksimal, true untuk fun => 15;
		return (self.fun >= c.MAXFUN)

	def IsHygieneEmpty(self):
		# Mengecek apakah nilai hygiene minimal, true untuk hygiene = 0;
		return (self.hygiene <= c.MINHYGIENE)
	
	def IsEnergyEmpty(self):
		# Mengecek apakah nilai energy minimal, true untuk energy = 0;
		return (self.energy <= c.MINENERGY)
	
	def IsFunEmpty(self):
		# Mengecek apakah nilai fun minimal, true untuk fun = 0;
		return (self.fun <= c.MINHYGIENE)
	
	def IsDie(self):
		# Mengecek kondisi mati, true saat nilai hygiene, energy dan fun = 0;
		return ((self.IsHygieneEmpty()) and (self.IsEnergyEmpty()) and (self.IsFunEmpty()))
	
	def IsFull(self):
		# Mengecek kondisi selesai, true saat nilai hygiene, energy dan fun = 15;
		return ((self.IsHygieneFull()) and (self.IsEnergyFull()) and (self.IsFunFull()))
	
	''' PROSEDUR AKSI '''
	def TidurSiang(self):
		# Prosedur aksi tidur siang
		# +10 Energy
		if(self.energy <= c.MAXENERGY-10):
			self.AddEnergy(10)
			self.TulisStatus()
		else:
			print("Aksi 'Tidur Siang' tidak valid")
	
	def TidurMalam(self):
		# Prosedur aksi tidur malam
		# +15 Energy
		if(self.energy <= c.MAXENERGY-15):
			self.AddEnergy(15)
			self.TulisStatus()
		else:
			print("Aksi 'Tidur Malam' tidak valid")
	
	def MakanHamburger(self):
		# Prosedur aksi makan hamburger
		# +5 Energy
		if(self.energy <= c.MAXENERGY-5):
			self.AddEnergy(5)
			self.TulisStatus()
		else:
			print("Aksi 'Makan Hamburger' tidak valid")
	
	def MakanPizza(self):
		# Prosedur aksi makan pizza
		# +10 Energy
		if(self.energy <= c.MAXENERGY-10):
			self.AddEnergy(10)
			self.TulisStatus()
		else:
			print("Aksi 'Makan Pizza' tidak valid")
	
	def MakanSteakAndBeans(self):
		# Prosedur aksi makan steak and beans
		# +15 Energy
		if(self.energy <= c.MAXENERGY-15):
			self.AddEnergy(15)
			self.TulisStatus()
		else:
			print("Aksi 'Makan Steak And Beans' tidak valid")
	
	def MinumAir(self):
		# Prosedur aksi minum air
		# -5 Hygiene
		if(self.hygiene >= c.MINHYGIENE+5):
			self.AddHygiene(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Minum Air' tidak valid")
	
	def MinumKopi(self):
		# Prosedur aksi minum kopi
		# +5 Energy -10 Hygiene
		if((self.energy <= c.MAXENERGY-5) and (self.hygiene >= c.MINHYGIENE+10)):
			self.AddHygiene(-10)
			self.AddEnergy(5)
			self.TulisStatus()
		else:
			print("Aksi 'Minum Kopi' tidak valid")
	
	def MinumJus(self):
		# Prosedur aksi minum jus
		# +10 Energy -5 Hygiene
		if((self.energy <= c.MAXENERGY-10) and (self.hygiene >= c.MINHYGIENE+5)):
			self.AddHygiene(-5)
			self.AddEnergy(10)
			self.TulisStatus()
		else:
			print("Aksi 'Minum Jus' tidak valid")
	
	def BuangAirKecil(self):
		# Prosedur aksi buang air kecil
		# +5 Hygiene
		if(self.hygiene <= c.MAXHYGIENE-5):
			self.AddHygiene(5)
			self.TulisStatus()
		else:
			print("Aksi 'Buang Air Kecil' tidak valid")
	
	def BuangAirBesar(self):
		# Prosedur aksi buang air besar
		# +10 Hygiene -5 Energy
		if((self.hygiene <= c.MAXHYGIENE-10) and (self.energy >= c.MINENERGY+5)):
			self.AddHygiene(10)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Buang Air Besar' tidak valid")
	
	def BersosialisasiKeKafe(self):
		# Prosedur aksi bersosialisasi ke kafe
		# +15 Fun -10 Energy -5 Hygiene
		if((self.hygiene >= c.MINHYGIENE+5) and (self.energy >= c.MINENERGY+10) and (self.fun <= c.MAXFUN-15)):
			self.AddHygiene(-5)
			self.AddEnergy(-10)
			self.AddFun(15)
			self.TulisStatus()
		else:
			print("Aksi 'Bersosialisasi ke Kafe' tidak valid")
	
	def BermainMediaSosial(self):
		# Prosedur aksi bermain media sosial
		# +10 Fun -10 Energy
		if((self.energy >= c.MINENERGY+10) and (self.fun <= c.MAXFUN-10)):
			self.AddEnergy(-10)
			self.AddFun(10)
			self.TulisStatus()
		else:
			print("Aksi 'Bermain Media Sosial' tidak valid")
	
	def BermainKomputer(self):
		# Prosedur aksi bermain komputer
		# +15 Fun -10 Energy
		if((self.energy >= c.MINENERGY+10) and (self.fun <= c.MAXFUN-15)):
			self.AddEnergy(-10)
			self.AddFun(15)
			self.TulisStatus()
		else:
			print("Aksi 'Bermain Komputer' tidak valid")
	
	def Mandi(self): 
		# Prosedur aksi mandi
		# +15 Hygiene -5 Energy
		if((self.hygiene <= c.MAXHYGIENE-15) and (self.energy >= c.MINENERGY+5)):
			self.AddHygiene(15)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Mandi' tidak valid")
	
	def CuciTangan(self):
		# Prosedur aksi cuci tangan
		# +5 Hygiene
		if(self.hygiene <= c.MAXHYGIENE-5):
			self.AddHygiene(5)
			self.TulisStatus()
		else:
			print("Aksi 'Cuci Tangan' tidak valid")
	
	def MendengarMusikDiRadio(self):
		# Prosedur aksi mendengar musik di radio 
		# +10 Fun -5 Energy
		if((self.fun <= c.MAXHYGIENE-10) and (self.energy >= c.MINENERGY+5)):
			self.AddFun(10)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Mendengar Musik di Radio' tidak valid")
	
	def MembacaKoran(self):
		# Prosedur aksi membaca koran
		# +5 Fun -5 Energy
		if((self.fun <= c.MAXHYGIENE-5) and (self.energy >= c.MINENERGY+5)):
			self.AddFun(5)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Membaca Koran' tidak valid")
	
	def MembacaNovel(self):
		# Prosedur aksi membaca novel
		# +10 Fun -5 Energy
		if((self.fun <= c.MAXHYGIENE-10) and (self.energy >= c.MINENERGY+5)):
			self.AddFun(10)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Membaca Novel' tidak valid")
