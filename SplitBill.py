# descrizione:
# la mia app deve ricevere come input: il valore totale della mia bolletta, il periodo relativo alla bolletta (esempio giugno 2021);
# il numero di giorni che il mio inquilino ha vissuto in casa;
# il nome di ogni inquilino;
# e in base a questi dati calcolare la quota di ogni inquilino;
# poi generare un reportpdf con queste info: nome inquilini, periodo, totale da pagare.



# bill:
        # valore_totale
        # periodo


# inquilino:
        # giorni a casa 
        # nome
        # paga (bill) 


# PdfReport:
        # filename 
        # crea() 






class bill: 
    def __init__ (self, totale, periodo):
        self.totale = totale 
        self.periodo = periodo 


class inquilino:
    def __init__ (self, nome, giorni_a_casa):
        self.nome = nome 
        self.giorni_a_casa = giorni_a_casa 
        

def paga (self):
    