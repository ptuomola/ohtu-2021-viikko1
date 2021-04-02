#adding a test comment
class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0.0):
        self.init_saldo(alku_saldo)
        self.init_tilavuus(tilavuus)

        if self.saldo > self.tilavuus:
            self.saldo = self.tilavuus

# this line is way tooo long 123123123123123123123123213123213123123213213123213213123123123123231232312131321323

    def init_tilavuus(self, tilavuus):
        if tilavuus < 0.0:
            self.tilavuus = 0
        else:
            self.tilavuus = tilavuus

    def init_saldo(self, alku_saldo):
        if alku_saldo > 0.0:
            self.saldo = alku_saldo
        else:
            self.saldo = 0


    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
