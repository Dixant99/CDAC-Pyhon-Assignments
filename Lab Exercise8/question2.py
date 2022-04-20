class songs:
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

happy_bday = songs(['May god bless you',
                       'Have a sunshine on you',
                       'Happy Birthday to you !'])
happy_bday.sing_me_a_song()
