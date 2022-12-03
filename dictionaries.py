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

    'stressed' : {},
    'sleepy': {},
    'tired' : {},
    'relaxed' : {},
    'restless' : {},
    'angry' : {},
    'calm' : {},
    'numb' : {},
    'irritaded' : {},
    'unimpressed': {},
    'mellow' : {}
    
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

    'stressed' : {},
    'sleepy': {},
    'tired' : {},
    'relaxed' : {},
    'restless' : {},
    'angry' : {},
    'calm' : {},
    'numb' : {},
    'irritaded' : {},
    'unimpressed': {},
    'mellow' : {}

}

dictonaryMood = {
    'happy': (dictSynonyms['happy'], dicAntonyms['happy']),

    'sad':  (dictSynonyms['sad'], dicAntonyms['sad']),

    'stressed' : (dictSynonyms['stressed'], dicAntonyms['stressed']),

    'sleepy': (dictSynonyms['sleepy'], dicAntonyms['sleepy']),

    'tired' : (dictSynonyms['tired'], dicAntonyms['tired']),

    'relaxed' : (dictSynonyms['relaxed'], dicAntonyms['relaxed']),

    'restless' : (dictSynonyms['restless'], dicAntonyms['restless']),

    'angry' : (dictSynonyms['angry'], dicAntonyms['angry']),

    'calm' : (dictSynonyms['calm'], dicAntonyms['calm']),

    'numb' : (dictSynonyms['numb'], dicAntonyms['numb']),

    'irritaded' : (dictSynonyms['irritaded'], dicAntonyms['irritaded']),

    # this should be an easter egg 'Surely you don't mean by my TP'
    'unimpressed' : (dictSynonyms['unimpressed'], dicAntonyms['unimpressed']), 

    'mellow' : (dictSynonyms['mellow'], dicAntonyms['mellow']),


}

dictionaryState = {

    'Negative': {},

    'Positive': {}

}



