import math
#questão 1.1
def questao1():
    print (5 **2)
    print (9 * 5)
    print (15 / 12)
    print (12 / 15)
    print (15 // 12)
    print(12 // 15)
    print(5 % 2)
    print(9 % 5)
    print(15 % 12)
    print(12 % 15)
    print(6 % 6)
    print(0%7)

#questão 2.1    
def questao2():
   return(51%24+14)
    

#questão 3.1     
def questao3():
    a=int(input("Digite horas atuais de 0 a 24: "))
    b=int(input("Digite horas que o alarme deve esperar: "))
    tempo=int((a+b)%24)
    print("A hora que o alarme irá tocar é: {} hora(s)".format(tempo))

#questão 4.1    
def questao4(a,b):
    from datetime import date
    a = date.today()
    futuro = date.fromordinal(a.toordinal()+b)
    dias = ('segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo')

    return dias[futuro.weekday()]
    

#questão 5.1    
def questao5():
    a=str("Só")
    b=str("trabalho")
    c=str("sem")
    d=str("diversão")
    e=str("faz")
    f=str("de")
    g=str("João")
    h=str("em") 
    i=str("chato")
    return print("{} {} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h,i))

#questão 1.2
def questao6():
    print ("6*1-2 =" , 6*1-2)
    print("6*(1-2)=" , 6*(1-2)) 

    #questão 2.2
def questao7():
    t=int(input("Digite o número de anos: "))
    p=10000
    n=12
    r=0.08
    a=p*(1+r/n)**(n*t)
    return print("O valor final depois de {} anos é : {:.2f} Reais".format(t,a))

#questão 3.2   
def questao8():
    r=float(input("Digite o valor do raio: "))
    pi=3.14
    a=pi*(r**2)
    return print(" A área do círculo com o raio de {:.2f} é de : {:.2f}".format(r,a))

#questão 4.2
def questao9(h,l):
    h=float(h)
    l=float(l)
    a=h*l 
    return print("A área do retângulo com a altura de {:.2f} e largura de {:.2f} é = {:.2f} ".format(h,l,a))

#questão 5.2    
def questao10(km,l):
    if l==0:
      print ("Valor não aceito ")
    else: 
      p=km/l
      print("A distancia percorida é de: {:.2f}".format(p))

#questão  6.2  
def questao11():
    c =float(input("digite o valor da temperatura em Celsius: "))
    f=float(((9/5)*c)+32)
    print("o resultado é : {:.2f} em graus Fahrenheit ".format(f))

#questao 7.2    
def questao12(f):
    c=float((5*(f-32))/9)
    return print("o resultado é : {:.2f} em graus Celsius ".format(c))
   