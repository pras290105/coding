class Hero:
    # class variable
    b = 0
    def __init__(self,inputName,inputHealth,inputPower,inputEnergy):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.energy = inputEnergy
        Hero.b += 1
    def serang(self,lawan):
        print(self.name,"Menyerang",lawan.name)
        self.energy -= 5
        print("Energi",self.name,"tersisa",self.energy)
        lawan.diserang(self,self.power)

    def diserang(self,lawan,power):
        print(self.name, "Diserang",lawan.name)
        s_diterima = power
        print("Serangan Diterima",s_diterima)
        self.health -= s_diterima
        print("Darah",self.name,"Tersisa",self.health)
       
        print("\n")



Miya = Hero("Miya",200,50,100)
Balmond = Hero("Balmond",500,10,100)
Tigreal = Hero("Tigreal",1000,5,100)
print("\t\tjumlah karakter [*] ",Hero.b)




Miya.serang(Tigreal)





