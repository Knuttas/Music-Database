# import helper functions from our database module
from database import run, get

"""
run('''
  INSERT INTO artists VALUES(NULL, 'Slayer', 'Best Metal band ever, no discussion!')
''')


run('''
  INSERT INTO artists VALUES(NULL, 'Ghost', 'Ghost, also formerly known as Ghost B.C. in the United States,[1] is a Swedish rock band that was formed in Linköping in 2006.!'),
  (NULL, 'Mastodon', 'Mastodon is an American heavy metal band from Atlanta, Georgia, formed in 2000.')
''')

run('''
  INSERT INTO albums VALUES(NULL, 'Reign in Blood', 'Reign in Blood is the third studio album by American thrash metal band Slayer, released on October 7, 1986, by Def Jam Recordings.', 1986, 1),
    (NULL, 'South of Heaven', 'South of Heaven is the fourth studio album by American thrash metal band Slayer, released on July 5, 1988 by Def Jam Recordings.', 1988, 1 ),
    (NULL, 'Seasons in the Abyss', 'Seasons in the Abyss is the fifth studio album by American thrash metal band Slayer, released on October 9, 1990, through Def American Records.', 1990, 1)
''')

run('''
  INSERT INTO albums VALUES(NULL, 'Opus Eponymous', 'Opus Eponymous (Latin for "self-titled work") is the debut studio album by the Swedish rock band Ghost.', 2010, 2),
    (NULL, 'Meliora', 'Meliora (Latin for "the pursuit of something better") is the third studio album by Swedish rock band Ghost.', 2015, 2),
    (NULL, 'Prequelle', 'Prequelle is the fourth studio album by the Swedish rock band Ghost.', 2018, 2)
''')

run('''
  INSERT INTO albums VALUES(NULL, 'Leviathan', 'Leviathan is the second album by American heavy metal band Mastodon, released in 2004 on Relapse Records.', 2004, 3),
    (NULL, 'Crack the Skye', 'Crack the Skye is the fourth studio album by American heavy metal band Mastodon, released on March 24, 2009 through Reprise, Sire and Relapse Records.', 2009, 3),
    (NULL, 'Blood and Mountain', 'Blood Mountain is the third full-length studio album and major label debut by American heavy metal band Mastodon.', NULL, 3)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'Angel of Death', 291 , 1),
    (NULL, 'Piece by Piece', 182, 1),
    (NULL, 'Necrophobic', 100, 1),
    (NULL, 'Altar of Sacrifice', 170, 1),
    (NULL, 'Jesus Saves', 174, 1),
    (NULL, 'Criminally Insane', 143, 1),
    (NULL, 'Reborn', 133, 1),
    (NULL, 'Epidemic', 143, 1),
    (NULL, 'Postmortem', 207, 1),
    (NULL, 'Raining Blood', 254, 1)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'South of Heaven', 298 , 2),
    (NULL, 'Silent Scream', 187, 2),
    (NULL, 'Live Undead', 230, 2),
    (NULL, 'Behind the Crooked Cross', 195, 2),
    (NULL, 'Mandatory Suicide', 245, 2),
    (NULL, 'Ghosts of War', 233, 2),
    (NULL, 'Read Between the Lies', 200, 2),
    (NULL, 'Cleanse the Soul', 182, 2),
    (NULL, 'Dissident Aggressor', 155, 2),
    (NULL, 'Spill the Blood', 288, 2)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'War Ensemble', 299 , 3),
    (NULL, 'Blood Red', 167, 3),
    (NULL, 'Spirit in Black', 247, 3),
    (NULL, 'Expendable Youth', 249, 3),
    (NULL, 'Dead Skin Mask', 320, 3),
    (NULL, 'Hallowed Point', 203, 3),
    (NULL, 'Skeletons of Society', 280, 3),
    (NULL, 'Temptation', 205, 3),
    (NULL, 'Born of Fire', 187, 3),
    (NULL, 'Seasons in the Abyss', 394, 3)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'Deus culpa', 94 , 4),
    (NULL, 'Con Clavi Con Dio', 213, 4),
    (NULL, 'Ritual', 268, 4),
    (NULL, 'Elizabeth', 241, 4),
    (NULL, 'Stand by Him', 236, 4),
    (NULL, 'Satan Prayer', 278, 4),
    (NULL, 'Death Knell', 276, 4),
    (NULL, 'Prime Mover', 233, 4),
    (NULL, 'Genesis', 243, 4)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'Spirit', 315 , 5),
    (NULL, 'From the Pinnacle to the Pit', 242, 5),
    (NULL, 'Cirice', 362, 5),
    (NULL, 'Spöksonat', 56, 5),
    (NULL, 'He Is', 253, 5),
    (NULL, 'Mummy Dust', 247, 5),
    (NULL, 'Majesty', 324, 5),
    (NULL, 'Devil Church', 66, 5),
    (NULL, 'Absolution', 290, 5),
    (NULL, 'Deus in Absentia', 337, 5)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'Ashes', 81 , 6),
    (NULL, 'Rats', 261, 6),
    (NULL, 'Faith', 269, 6),
    (NULL, 'See the Light', 245, 6),
    (NULL, 'Miasma', 317, 6),
    (NULL, 'Dance Macabre', 219, 6),
    (NULL, 'Pro Memoria', 339, 6),
    (NULL, 'Witch Image', 210, 6),
    (NULL, 'Helvetesfönster', 355, 6),
    (NULL, 'Life Eternal', 207, 6)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'Blood and Thunder', 228 , 7),
    (NULL, 'I Am Ahab', 165, 7),
    (NULL, 'Seabeast', 255, 7),
    (NULL, 'Island', 206, 7),
    (NULL, 'Iron Tusk', 183, 7),
    (NULL, 'Megalodon', 262, 7),
    (NULL, 'Naked Burn', 222, 7),
    (NULL, 'Aqua Dementia', 250, 7),
    (NULL, 'Hearts Alive', 819, 7),
    (NULL, 'Joseph Merrick', 213, 7)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'Oblivion', 346 , 8),
    (NULL, 'Divinations', 218, 8),
    (NULL, 'Quintessence', 327, 8),
    (NULL, 'The Czar', 654, 8),
    (NULL, 'Ghost of Karelia', 324, 8),
    (NULL, 'Crack the Skye', 354, 8),
    (NULL, 'The Last Baron', 780, 8)
''')

run('''
  INSERT INTO songs VALUES(NULL, 'The Wolf is Loose', 214 , 9),
    (NULL, 'Crystal Skull', 207, 9),
    (NULL, 'Sleeping Giant', 336, 9),
    (NULL, 'Capillarian Crest', 265, 9),
    (NULL, 'Circle of Cysquatch', 200, 9),
    (NULL, 'Bladecatcher', 200, 9),
    (NULL, 'Colony of Birchmen', 260, 9),
    (NULL, 'Hunters of the Sky', 232, 9),
    (NULL, 'Hand of Stone', 210, 9),
    (NULL, 'This Mortal Soil', 300, 9),
    (NULL, 'Siberian Divide', 332, 9),
    (NULL, 'Pendulous Skin', 306, 9)
''')
"""