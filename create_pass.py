import random
import string

class Create_Pass:
    def __init__(self,pass_length:int,lw:float,uw:float,sw:float,nw:float) -> None:
        self.pass_length=pass_length                    #şifre uzunluğu
        
        self.pcs_lw=round(self.pass_length*lw)            #küçük harf sayısı
        self.pcs_uw=round(self.pass_length*uw)            #büyük harf sayısı
        self.pcs_sw=round(self.pass_length*sw)            #sembol sayısı
        self.pcs_nw=round(self.pass_length*nw)            #numara sayısı
        
    def yaz(self):
        print(f"len={self.pass_length} lw={self.pcs_lw} uw={self.pcs_uw} sw={self.pcs_sw} nw={self.pcs_nw}")
        
    def shuf_data(self,data:list,repeats:int)->list:    #listedeki verileri karıştırma
        result = []                                     #repeats karakter tekrar edebilme sayısı
        if repeats==0:                                  #repeats değeri 0 ise tekrar kontrolü yapmaz
            result=data
        else:
            for d in data:
                for _ in range(repeats):
                    result.append(d)
        random.shuffle(result)  
        return result
    
    def str_pass(self,data:list)->str:                  #listedeki verileri birleştirip string oluşturur                
        pass_w=''
        for item in data:
            pass_w=pass_w+str(item)
        return pass_w
    
    def create_sw(self)->list:                          #şifre için gerekli sembolleri içeren listeyi verir
        symbol=string.punctuation
        unique=random.sample(symbol,self.pcs_sw)
        return unique
    
    def create_lw(self)->list:                          #şifre için gerekli küçük harfleri içeren listeyi verir
        symbol=string.ascii_lowercase+"\u011F\u00FC\u015F\u0131\u00F6\u00E7"
        unique=random.sample(symbol,self.pcs_lw)
        return unique
    
    def create_uw(self)->list:                          #şifre için gerekli sbüyük harfleri içeren listeyi verir
        symbol=string.ascii_uppercase+"\u011E\u00DC\u015E\u0130\u00D6\u00C7"
        unique=random.sample(symbol,self.pcs_uw)
        return unique
    
    def create_nw(self)->list:                          #şifre için gerekli rakamları içeren listeyi verir
        unique=[]
        for _ in range(self.pcs_nw):
            symbol=random.randint(0,9)
            unique.append(symbol)
        return unique
    
    def generate_pass(self)->str:                       #şifreyi oluşturan fonksiyon
        sw=self.create_sw()
        lw=self.create_lw()
        uw=self.create_uw()
        nw=self.create_nw()
        print(f"len={self.pass_length} lw={lw} uw={uw} sw={sw} nw={nw}")
        data=sw+lw+uw+nw
        shuf=self.shuf_data(data,0)
        pass_str=self.str_pass(shuf)
        return pass_str             
 
#Harf oranları toplamı 1 olacak şekilde ayarlayın
pw=16                       #kelime uzunluğu !!çift sayı giriniz!!
lw=0.50                     #küçük harf oranı
uw=0.30                     #büyük harf oranı
sw=0.10                     #sembol oranı
nw=0.10                     #rakam oranı
print(f"top={pw*lw+uw*pw+pw*sw+pw*nw}")
print(f"pw={lw+uw+sw+nw}")
ct = Create_Pass(pw,lw,uw,sw,nw)
ct.yaz() 
p = ct.generate_pass()  
print(p)
print(len(p))

