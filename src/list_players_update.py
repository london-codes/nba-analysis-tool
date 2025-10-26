from make_csv import update_player_csv


"""
Module for updating or creating player CSVs from Basketball Reference.

Usage:
    - Use update_player_csv(url, player_name) to update an existing csv file with the name inputed or add a 
    player not already in the data base.
    - To add a player you need to navigate to basketball reference and find the gamelog page with the specifc year
    you want.

Important Notes:
    - 5 second limit between each call of the update_player_csv function to avoid the rate limit and being blocked.

"""
    #   updates:

#ATL
#update_player_csv('https://www.basketball-reference.com/players/k/kennalu01/gamelog/2025','luke') # no 2025
update_player_csv('https://www.basketball-reference.com/players/o/okongon01/gamelog/2025','onyeka')
update_player_csv('https://www.basketball-reference.com/players/j/johnsja05/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/y/youngtr01/gamelog/2025','trae')
update_player_csv('https://www.basketball-reference.com/players/d/daniedy01/gamelog/2025','dyson')
#update_player_csv('https://www.basketball-reference.com/players/p/porzikr01/gamelog/2025','kristaps') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/a/alexani01/gamelog/2025','nickeil') # no 2025

#bos
update_player_csv('https://www.basketball-reference.com/players/p/pritcpa01/gamelog/2025','payton')
update_player_csv('https://www.basketball-reference.com/players/w/whitede01/gamelog/2025','derrick')
update_player_csv('https://www.basketball-reference.com/players/h/hausesa01/gamelog/2025','sam')
update_player_csv('https://www.basketball-reference.com/players/q/quetane01/gamelog/2025','neemias')
update_player_csv('https://www.basketball-reference.com/players/b/brownja02/gamelog/2025','jaylen')
#update_player_csv('https://www.basketball-reference.com/players/s/simonan01/gamelog/2025','anfernee') # no 2025


#cha / cho

update_player_csv('https://www.basketball-reference.com/players/b/bridgmi02/gamelog/2025','miles')
update_player_csv('https://www.basketball-reference.com/players/b/ballla01/gamelog/2025','lamelo')
update_player_csv('https://www.basketball-reference.com/players/m/millebr02/gamelog/2025','brandon')
update_player_csv('https://www.basketball-reference.com/players/m/manntr01/gamelog/2025','tre')
update_player_csv('https://www.basketball-reference.com/players/s/salauti01/gamelog/2025','tidjane')
update_player_csv('https://www.basketball-reference.com/players/d/diabamo01/gamelog/2025','moussa')
#update_player_csv('https://www.basketball-reference.com/players/s/sextoco01/gamelog/2025','collin') # no 2025
# update_player_csv('https://www.basketball-reference.com/players/j/jamessi01/gamelog/2026','kion') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/k/kalkbry01/gamelog/2026','ryan') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/k/knuepko01/gamelog/2026','kon') # no 2025

#det
update_player_csv('https://www.basketball-reference.com/players/s/stewais01/gamelog/2025','isaiah')
update_player_csv('https://www.basketball-reference.com/players/c/cunnica01/gamelog/2025','cade')
update_player_csv('https://www.basketball-reference.com/players/d/durenja01/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/t/thompau01/gamelog/2025','ausar')
update_player_csv('https://www.basketball-reference.com/players/h/harrito02/gamelog/2025','tobias')
update_player_csv('https://www.basketball-reference.com/players/h/hollaro01/gamelog/2025','ron')
#update_player_csv('https://www.basketball-reference.com/players/r/robindu01/gamelog/2025','duncan') # no 2025

"""
# chi
update_player_csv('https://www.basketball-reference.com/players/w/willipa01/gamelog/2025','patrick')
update_player_csv('https://www.basketball-reference.com/players/v/vucevni01/gamelog/2025','nikola')
update_player_csv('https://www.basketball-reference.com/players/d/dosunay01/gamelog/2025','ayo')
update_player_csv('https://www.basketball-reference.com/players/g/giddejo01/gamelog/2025','josh')
update_player_csv('https://www.basketball-reference.com/players/s/smithja04/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/b/buzelma01/gamelog/2025','matas')
#update_player_csv('https://www.basketball-reference.com/players/h/huertke01/gamelog/2025','kevin') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/j/jonestr01/gamelog/2025','tre') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/o/okorois01/gamelog/2025','isaac') # no 2025


#cleveland
update_player_csv('https://www.basketball-reference.com/players/a/allenja01/gamelog/2025','jarrett')
update_player_csv('https://www.basketball-reference.com/players/m/mobleev01/gamelog/2025','evan')
update_player_csv('https://www.basketball-reference.com/players/m/merrisa01/gamelog/2025','sam')
update_player_csv('https://www.basketball-reference.com/players/m/mitchdo01/gamelog/2025','donovan')
update_player_csv('https://www.basketball-reference.com/players/t/tysonja01/gamelog/2025','jaylon')
#update_player_csv('https://www.basketball-reference.com/players/h/huntede01/gamelog/2025','de andre') only played last half of season with cle
#update_player_csv('https://www.basketball-reference.com/players/b/balllo01/gamelog/2025','lonzo') no 2025 was on chi

#den
update_player_csv('https://www.basketball-reference.com/players/m/murraja01/gamelog/2025','jamal')
update_player_csv('https://www.basketball-reference.com/players/g/gordoaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/b/braunch01/gamelog/2025','christian')
update_player_csv('https://www.basketball-reference.com/players/w/watsope01/gamelog/2025','peyton')
#update_player_csv('https://www.basketball-reference.com/players/b/brownbr01/gamelog/2025','bruce') # no 2025
update_player_csv('https://www.basketball-reference.com/players/j/jokicni01/gamelog/2025','nikola')
#update_player_csv('https://www.basketball-reference.com/players/j/johnsca02/gamelog/2025','cameron') # no 2025


#Golden state
#update_player_csv('https://www.basketball-reference.com/players/h/horfoal01/gamelog/2025','al') no 2025 was on bos
update_player_csv('https://www.basketball-reference.com/players/c/curryst01/gamelog/2025','curry')
update_player_csv('https://www.basketball-reference.com/players/b/butleji01/gamelog/2025','butler')
update_player_csv('https://www.basketball-reference.com/players/g/greendr01/gamelog/2025','draymond')
update_player_csv('https://www.basketball-reference.com/players/k/kuminjo01/gamelog/2025','jonathan')
update_player_csv('https://www.basketball-reference.com/players/p/podzibr01/gamelog/2025','brandin')
update_player_csv('https://www.basketball-reference.com/players/h/hieldbu01/gamelog/2025','buddy')

#ind
update_player_csv('https://www.basketball-reference.com/players/n/nembhan01/gamelog/2025','andrew')
update_player_csv('https://www.basketball-reference.com/players/n/nesmiaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/m/mathube01/gamelog/2025','bennedict')
update_player_csv('https://www.basketball-reference.com/players/s/siakapa01/gamelog/2025','pascal')
#update_player_csv('https://www.basketball-reference.com/players/p/peterta01/gamelog/2026','taelon') # no 2025
update_player_csv('https://www.basketball-reference.com/players/t/toppiob01/gamelog/2025','obi')

# mem
update_player_csv('https://www.basketball-reference.com/players/j/jacksja02/gamelog/2025','jaren')
update_player_csv('https://www.basketball-reference.com/players/m/moranja01/gamelog/2025','ja')
update_player_csv('https://www.basketball-reference.com/players/a/aldamsa01/gamelog/2025','santi')
update_player_csv('https://www.basketball-reference.com/players/w/wellsja01/gamelog/2025','jaylen')
#update_player_csv('https://www.basketball-reference.com/players/l/landajo01/gamelog/2025','jock') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/c/caldwke01/gamelog/2025','kentavious') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/s/smallja01/gamelog/2026','javon') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/c/cowarce01/gamelog/2026','cedric') # no 2025


#min
update_player_csv('https://www.basketball-reference.com/players/r/reidna01/gamelog/2025','naz')
update_player_csv('https://www.basketball-reference.com/players/m/mcdanja02/gamelog/2025','jaden')
update_player_csv('https://www.basketball-reference.com/players/g/goberru01/gamelog/2025','rudy')
update_player_csv('https://www.basketball-reference.com/players/c/conlemi01/gamelog/2025','mike')
update_player_csv('https://www.basketball-reference.com/players/e/edwaran01/gamelog/2025','anthony')
update_player_csv('https://www.basketball-reference.com/players/r/randlju01/gamelog/2025','julius')
update_player_csv('https://www.basketball-reference.com/players/d/divindo01/gamelog/2025','donte')

#nyk
update_player_csv('https://www.basketball-reference.com/players/r/robinmi01/gamelog/2025','mitchell') # did not play like entire 3/4 2025
update_player_csv('https://www.basketball-reference.com/players/m/mcbrimi01/gamelog/2025','miles')
update_player_csv('https://www.basketball-reference.com/players/h/hartjo01/gamelog/2025','josh')
update_player_csv('https://www.basketball-reference.com/players/a/anunoog01/gamelog/2025','OG')
update_player_csv('https://www.basketball-reference.com/players/b/brunsja01/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/b/bridgmi01/gamelog/2025','mikal')
update_player_csv('https://www.basketball-reference.com/players/t/townska01/gamelog/2025','karl-anthony')
#update_player_csv('https://www.basketball-reference.com/players/y/yabusgu01/gamelog/2025','guershon') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/c/clarkjo01/gamelog/2025','jordan') # no 2025

# orlando
update_player_csv('https://www.basketball-reference.com/players/c/cartewe01/gamelog/2025','wendell')
update_player_csv('https://www.basketball-reference.com/players/s/suggsja01/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/w/wagnefr01/gamelog/2025','franz')
update_player_csv('https://www.basketball-reference.com/players/b/blackan01/gamelog/2025','anthony')
update_player_csv('https://www.basketball-reference.com/players/b/banchpa01/gamelog/2025','paolo') # played last half 2025
#update_player_csv('https://www.basketball-reference.com/players/b/banede01/gamelog/2025','desmond') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/j/jonesty01/gamelog/2025','tyus') # no 2025

#okc
update_player_csv('https://www.basketball-reference.com/players/g/gilgesh01/gamelog/2025','shai')
update_player_csv('https://www.basketball-reference.com/players/d/dortlu01/gamelog/2025','luguentz')
update_player_csv('https://www.basketball-reference.com/players/w/wiggiaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/h/holmgch01/gamelog/2025','chet')
update_player_csv('https://www.basketball-reference.com/players/w/wallaca01/gamelog/2025','cason')
update_player_csv('https://www.basketball-reference.com/players/c/carusal01/gamelog/2025','alex')
update_player_csv('https://www.basketball-reference.com/players/h/harteis01/gamelog/2025','isaiah')

#phi

update_player_csv('https://www.basketball-reference.com/players/o/oubreke01/gamelog/2025','kelly')
update_player_csv('https://www.basketball-reference.com/players/e/embiijo01/gamelog/2025','joel') # bareley 2025
update_player_csv('https://www.basketball-reference.com/players/m/maxeyty01/gamelog/2025','tyrese')
update_player_csv('https://www.basketball-reference.com/players/b/bonaad01/gamelog/2025','adem')
#update_player_csv('https://www.basketball-reference.com/players/g/grimequ01/gamelog/2025','quentin') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/b/barlodo01/gamelog/2025','dominick') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/e/edgecvj01/gamelog/2026','vj') # no 2025


#pho/phx
update_player_csv('https://www.basketball-reference.com/players/a/allengr01/gamelog/2025','grayson')
update_player_csv('https://www.basketball-reference.com/players/o/onealro01/gamelog/2025','royce')
update_player_csv('https://www.basketball-reference.com/players/b/bookede01/gamelog/2025','devin')
update_player_csv('https://www.basketball-reference.com/players/d/dunnry01/gamelog/2025','ryan')
update_player_csv('https://www.basketball-reference.com/players/i/ighodos01/gamelog/2025','oso')
update_player_csv('https://www.basketball-reference.com/players/g/gilleco01/gamelog/2025','collin') # played last half 2025
#update_player_csv('https://www.basketball-reference.com/players/b/brookdi01/gamelog/2025','dillon') # no 2025



#tor
update_player_csv('https://www.basketball-reference.com/players/p/poeltja01/gamelog/2025','jakob')
update_player_csv('https://www.basketball-reference.com/players/d/dickgr01/gamelog/2025','gradey')
update_player_csv('https://www.basketball-reference.com/players/b/barrerj01/gamelog/2025','RJ')
update_player_csv('https://www.basketball-reference.com/players/q/quickim01/gamelog/2025','immanuel') #injuired a lot 2025
update_player_csv('https://www.basketball-reference.com/players/b/barnesc01/gamelog/2025','scottie')
#update_player_csv('https://www.basketball-reference.com/players/i/ingrabr01/gamelog/2025','brandon') no 2025

"""





