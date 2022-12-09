#################################################
#dictionary.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
dictSynonyms = {
    'happy': 
        {
         'cheerful','contented','delighted','ecstatic','elated','glad',
         'joyful','joyous','jubilant','lively','merry','overjoyed','peaceful',
         'pleasant','pleased','satisfied','thrilled', 'upbeat'
        },

    'sad':   
        {
         'bitter', 'dismal', 'melancholic', 'mournful', 'pessimistic', 'somber',
         'sorrowful', 'sorry', 'unhappy', 'blue', 'cheerless', 'dejected',
         'depressed'
        },

    'stressed' :
        {
         'harassed', 'harrowed','peaked','pinched','sapped','starved',
         'strained','thin','tired','worn','fraught','haggard'
        },
    'excited': 
        {
          'thrilled', 'pumped', 'eager', 'keen', 'ready', 'ardent', 'zealous', 
          'happy' 
        },
    'tired' : 
        {
         'drainrd', 'slow', 'lethargic', 'sleepy', 'faint', 'droopy', 'weary', 
         'beat', 'lethargic'
        },

    'relaxed' : 
        {'easeful', 'easygoing','rested','fresh','unconcerned','carefree',
         'lighthearted','laid-back'
        },

    'restless' : {},
    'angry' : {},
    'calm' : {},
    'curious' : {},
    'irritated' : {},
    'unimpressed': {},
    'pleased' : {}
    
}

dicAntonyms = {
    'happy': 
        {
         'depressed', 'down', 'melancholy', 'miserable', 'sad', 
         'sorrowful', 'troubled', 'unhappy', 'upset', 'discouraged'
        },
 
    'sad':
        {
         'cheerful','glad','happy','hopeful', 'joyful', 'cheerful', 'overjoyed',
         'joyful'
        },

    'stressed' : 
        {
         'rested','fresh','relaxed','unconcerned','carefree','lighthearted','laid-back'
        },

    'excited': {'bored', 'tired', 'jaded', 'aloof', 'placid' , 'uniterested'},
    'tired' : 
        {
         'thrilled', 'pumped', 'eager', 'keen', 'ready', 'ardent', 'zealous', 
         'happy' 
        },
    'relaxed' : 
        {
         'harassed', 'harrowed','peaked','pinched','sapped','starved',
         'strained','thin','tired','worn','fraught','haggard'
        },
    'restless' : {},
    'angry' : {},
    'calm' : {},
    'curious' : {},
    'irritated' : {},
    'unimpressed': {},
    'pleased' : {}


}

dictonaryMood = {
    'happy': (dictSynonyms['happy'], dicAntonyms['happy']),

    'sad':  (dictSynonyms['sad'], dicAntonyms['sad']),

    'stressed' : (dictSynonyms['stressed'], dicAntonyms['stressed']),

    'excited': (dictSynonyms['excited'], dicAntonyms['excited']),

    'tired' : (dictSynonyms['tired'], dicAntonyms['tired']),

    'relaxed' : (dictSynonyms['relaxed'], dicAntonyms['relaxed']),

    'restless' : (dictSynonyms['restless'], dicAntonyms['restless']),

    'angry' : (dictSynonyms['angry'], dicAntonyms['angry']),

    'calm' : (dictSynonyms['calm'], dicAntonyms['calm']),

    'curious' : (dictSynonyms['curious'], dicAntonyms['curious']),

    'irritated' : (dictSynonyms['irritated'], dicAntonyms['irritated']),

    'unimpressed' : (dictSynonyms['unimpressed'], dicAntonyms['unimpressed']), 

    'pleased' : (dictSynonyms['pleased'], dicAntonyms['pleased']),


}

dictionaryType = {

    'Positive': {'happy','excited','pleased','calm','relaxed','curious'},

    'Negative': {'sad','stressed','tired','restless','angry','irritated',
                 'unimpressed'
                }

}

