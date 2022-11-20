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
        }
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
        }

}

dictonaryMood = {
    'happy': (dictSynonyms['happy'], dicAntonyms['happy']),

    'sad':  (dictSynonyms['sad'], dicAntonyms['sad']),

    'stressed' : {},

    'sleepy': {},

    'tired' : {},

    'relaxed' : {},

    'restless' : {},

    'angry' : {},

    'calm' : {},

    'numb' : {}, # Lol Me

    'irritaded' : {},

    'unimpressed' : {}, # this should be an easter egg 'Surely you don't mean TP

    'mellow' : {}


}



dictionaryState = {

    'awake': {'alive','attentive','aware','cognizant','vigilant'}


}