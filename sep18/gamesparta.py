
#  while loop  example

deamon = """ 
              ,   .-'"'=;_  ,
              |\.'-~`-.`-`;/|
              \.` '.'~-.` './
              (\`,__=-'__,'/)
           _.-'-.( d\_/b ).-'-._
         /'.-'   ' .---. '   '-.`\ 
       /'  .' (=    (_)    =) '.  `\ 
      /'  .',  `-.__.-.__.-'  ,'.  `\ 
     (     .'.   V       V  ; '.     )
     (    |::  `-,__.-.__,-'  ::|    )
     |   /|`:.               .:'|\   |
     |  / | `:.              :' |`\  |
     | |  (  :.             .:  )  | |
     | |   ( `:.            :' )   | |
     | |    \ :.           .: /    | |
     | |     \`:.         .:'/     | |
     ) (      `\`:.     .:'/'      ) (
     (  `)_     ) `:._.:' (     _(`  )
     \  ' _)  .'           `.  (_ `  /
      \  '_) /   .'"```"'.   \ (_`  /
       `'"`  \  (         )  /  `"'`
   ___   jgs  `.`.       .'.'        ___
 .`   ``"""'''--`_)     (_'--'''"""``   `.
(_(_(___...--'"'`         `'"'--...___)_)_)

"""
sword ="""       
      /| ________________
O|===|* >________________>
      \|
      """

print("Game rules: use your dagger to defeat the army of Xerox ! ")
print("Note: One keyboard hit is considered as one stike of your sword ! ")

answer = input("Ready ?\n")
count = 5  

if answer != "yes":
    print("There will be no glory in your sacrifice son. Where is King Leonidas ? ")
else:
    print("Go ~!")
    print(deamon)
    while count >0:
        input("\n")
        print(sword)
        print("screech ! grunt, ugh ! #$%!@#$%^&&*()*&%$$##@@!!@##$$$zz@#%\n")
        count -=1

    print("wow ! you defeated the deamon !")
    print("This is Sparrrrrrrrrrrrrrrrrrrrrrrrrrrrtaaaaaaaaaaaaa! ")

