# Nama File : sims.c 
# Tanggal: 19 September 2019
# Topik: Tubes TBFO

import constant as c

class Status:
	''' KONSTRUKTOR '''
	def __init__(self):
		'''Defines  variables'''
		self.hygiene = 0
		self.energy = 0
		self.fun = 0
        
	def __init__(self, h, e, f):
		'''Defines  variables'''
		self.hygiene = h
		self.energy = e
		self.fun = f	

	def Start(self):
		self.hygiene = 0
		self.energy = 10
		self.fun = 0
	
	''' SELEKTOR '''
	def AddHygiene(self,h):
		self.hygiene += (h)
	
	def AddEnergy(self,e):
		self.energy += (e)
		
	def AddFun(self,f):
		self.fun += (f)
	
	''' INPUT/OUTPUT '''
	def TulisStatus(self):
		print("***********STATUS************")
		print("Hygiene	= " + str(self.hygiene))
		print("Energy	= " + str(self.energy))
		print("Fun	= " + str(self.fun))
	
	def BacaStatus(self):
		print("*********BACA STATUS**********")
		
		self.hygiene = int(input("Masukkan nilai Hygiene	: "))
		while (not(self.IsHygieneValid())):
			print("Nilai Hygiene tidak Valid")
			self.hygiene = int(input("Masukkan nilai Hygiene	: "))
		
		self.energy = int(input("Masukkan nilai Energy	: "))
		while (not(self.IsEnergyValid())):	
			print("Nilai Energy tidak Valid")
			self.energy = int(input("Masukkan nilai Energy	: "))
		
		self.fun = int(input("Masukkan nilai Fun	: "))
		while (not(self.IsFunValid())):
			print("Nilai Fun tidak Valid")
			self.fun = int(input("Masukkan nilai Fun	: "))
			
	def TulisAksi(self):
		print("*********LIST AKSI**********")
		print("Ketikkan keyword yang akan dipilih kemudian 'enter', misal: Tidur Siang")
		print("List Keyword Aksi: ")
		print("1. Tidur Siang", end="			"); print("10. Buang Air Besar")
		print("2. Tidur Malam",  end="			");	print("11. Bersosialisasi ke Kafe")
		print("3. Makan Hamburger",  end="		"); print("12. Bermain Media Sosial")
		print("4. Makan Pizza",  end="			"); print("13. Bermain Komputer")
		print("5. Makan Steak and Beans",  end="	"); print("14. Mandi")
		print("6. Minum Air",  end="			"); print("15. Cuci Tangan")
		print("7. Minum Kopi",  end="			"); print("16. Mendengar Musik di Radio")
		print("8. Minum Jus",  end="			"); print("17. Membaca Koran")
		print("9. Buang Air Kecil", end="		"); print("18. Membaca Novel")
	
	def BacaAksi(self):
		self.TulisAksi()
		print("****************************")
		print("Ketikkan Aksi sesuai Keyword yang diberikan")
		print("Ketik 'Menu' untuk kembali ke menu")		
		print("****************************")
		Baca = str(input("Keyword Aksi: "))
		Baca = Baca.lower()
		while(Baca != "menu"):
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
			else:
				print("Aksi Tidak Tersedia")
			print("****************************")
			Baca = str(input("Keyword Aksi: "))
			Baca = Baca.lower()

		self.BacaMenu()
		
	def TulisMenu(self):
		print("*********LIST MENU**********")
		print("Ketikkan keyword yang akan dipilih kemudian 'enter', misal: Bermain")
		print("List Menu THE SIMS: ")
		print("1. Bermain")
		print("2. Cek Status")
		print("3. Ubah Status")
		print("4. Tampilkan Menu")
		print("5. Tampilkan Aksi")
		print("6. EXIT")
	
	def BacaMenu(self):
		self.TulisMenu()
		print("****************************")
		Pilih = str(input("Keyword Menu: "))
		Pilih = Pilih.lower()
		while (Pilih != "exit"):
			if(Pilih == "bermain"):
				self.BacaAksi()
			elif(Pilih == "cek status"):
				self.TulisStatus()
			elif(Pilih == "ubah status"):
				self.BacaStatus()
			elif(Pilih == "tampilkan menu"):
				self.TulisMenu()
			elif(Pilih == "tampilkan aksi"):
				self.TulisAksi()
			else:
				print("Menu tidak tersedia")	
			print("****************************")
			Pilih = str(input("Keyword Menu: "))
			Pilih = Pilih.lower()
		
	''' PREDIKAT '''
	def IsHygieneValid(self):
		return ((self.hygiene >= c.MINHYGIENE) and (self.hygiene <= c.MAXHYGIENE))
	
	def IsEnergyValid(self):
		return ((self.energy >= c.MINENERGY) and (self.energy <= c.MAXENERGY))
	
	def IsFunValid(self):
		return ((self.fun >= c.MINFUN) and (self.fun <= c.MAXFUN))
	
	def IsHygieneFull(self):
		return (self.hygiene >= c.MAXHYGIENE)
	
	def IsEnergyFull(self):
		return (self.energy >= c.MAXENERGY)
	
	def IsFunFull(self):
		return (self.fun >= c.MAXFUN)

	def IsHygieneEmpty(self):
		return (self.hygiene <= c.MINHYGIENE)
	
	def IsEnergyEmpty(self):
		return (self.energy <= c.MINENERGY)
	
	def IsFunEmpty(self):
		return (self.fun <= c.MINHYGIENE)
	
	def IsDie(self):
		return ((self.IsHygieneEmpty()) and (self.IsEnergyEmpty()) and (self.IsFunEmpty()))
	
	''' PROSEDUR AKSI '''
	def TidurSiang(self):
		if(self.energy <= c.MAXENERGY-10):
			self.AddEnergy(10)
			self.TulisStatus()
		else:
			print("Aksi 'Tidur Siang' tidak valid")
	
	def TidurMalam(self):
		# +15 Energy
		if(self.energy <= c.MAXENERGY-15):
			self.AddEnergy(15)
			self.TulisStatus()
		else:
			print("Aksi 'Tidur Malam' tidak valid")
	
	def MakanHamburger(self):
		# +5 Energy
		if(self.energy <= c.MAXENERGY-5):
			self.AddEnergy(5)
			self.TulisStatus()
		else:
			print("Aksi 'Makan Hamburger' tidak valid")
	
	def MakanPizza(self):
		# +10 Energy
		if(self.energy <= c.MAXENERGY-10):
			self.AddEnergy(10)
			self.TulisStatus()
		else:
			print("Aksi 'Makan Pizza' tidak valid")
	
	
	def MakanSteakAndBeans(self):
		# +15 Energy
		if(self.energy <= c.MAXENERGY-15):
			self.AddEnergy(15)
			self.TulisStatus()
		else:
			print("Aksi 'Makan Steak And Beans' tidak valid")
	
	def MinumAir(self):
		# -5 Hygiene
		if(self.hygiene >= c.MINHYGIENE+5):
			self.AddHygiene(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Minum Air' tidak valid")
	
	def MinumKopi(self):
		# +5 Energy -10 Hygiene
		if((self.energy <= c.MAXENERGY-5) and (self.hygiene >= c.MINHYGIENE+10)):
			self.AddHygiene(-10)
			self.AddEnergy(5)
			self.TulisStatus()
		else:
			print("Aksi 'Minum Kopi' tidak valid")
	
	def MinumJus(self):
		# +10 Energy -5 Hygiene
		if((self.energy <= c.MAXENERGY-10) and (self.hygiene >= c.MINHYGIENE+5)):
			self.AddHygiene(-5)
			self.AddEnergy(10)
			self.TulisStatus()
		else:
			print("Aksi 'Minum Jus' tidak valid")
	
	def BuangAirKecil(self):
		# +5 Hygiene
		if(self.hygiene <= c.MAXHYGIENE-5):
			self.AddHygiene(5)
			self.TulisStatus()
		else:
			print("Aksi 'Buang Air Kecil' tidak valid")
	
	def BuangAirBesar(self):
		# +10 Hygiene -5 Energy
		if((self.hygiene <= c.MAXHYGIENE-10) and (self.energy >= c.MINENERGY+5)):
			self.AddHygiene(10)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Buang Air Besar' tidak valid")
	
	def BersosialisasiKeKafe(self):
		# +15 Fun -10 Energy -5 Hygiene
		if((self.hygiene >= c.MINHYGIENE+5) and (self.energy >= c.MINENERGY+10) and (self.fun <= c.MAXFUN-15)):
			self.AddHygiene(-5)
			self.AddEnergy(-10)
			self.AddFun(15)
			self.TulisStatus()
		else:
			print("Aksi 'Bersosialisasi ke Kafe' tidak valid")
	
	def BermainMediaSosial(self):
		# +10 Fun -10 Energy
		if((self.energy >= c.MINENERGY+10) and (self.fun <= c.MAXFUN-10)):
			self.AddEnergy(-10)
			self.AddFun(10)
			self.TulisStatus()
		else:
			print("Aksi 'Bermain Media Sosial' tidak valid")
	
	def BermainKomputer(self):
		# +15 Fun -10 Energy
		if((self.energy >= c.MINENERGY+10) and (self.fun <= c.MAXFUN-15)):
			self.AddEnergy(-10)
			self.AddFun(15)
			self.TulisStatus()
		else:
			print("Aksi 'Bermain Komputer' tidak valid")
	
	def Mandi(self): 
		# +15 Hygiene -5 Energy
		if((self.hygiene <= c.MAXHYGIENE-15) and (self.energy >= c.MINENERGY+5)):
			self.AddHygiene(15)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Mandi' tidak valid")
	
	def CuciTangan(self):
		# +5 Hygiene
		if(self.hygiene <= c.MAXHYGIENE-5):
			self.AddHygiene(5)
			self.TulisStatus()
		else:
			print("Aksi 'Cuci Tangan' tidak valid")
	
	def MendengarMusikDiRadio(self): 
		# +10 Fun -5 Energy
		if((self.fun <= c.MAXHYGIENE-10) and (self.energy >= c.MINENERGY+5)):
			self.AddFun(10)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Mendengar Musik di Radio' tidak valid")
	
	def MembacaKoran(self):
		# +5 Fun -5 Energy
		if((self.fun <= c.MAXHYGIENE-5) and (self.energy >= c.MINENERGY+5)):
			self.AddFun(5)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Membaca Koran' tidak valid")
	
	def MembacaNovel(self):
		# +10 Fun -5 Energy
		if((self.fun <= c.MAXHYGIENE-10) and (self.energy >= c.MINENERGY+5)):
			self.AddFun(10)
			self.AddEnergy(-5)
			self.TulisStatus()
		else:
			print("Aksi 'Membaca Novel' tidak valid")
