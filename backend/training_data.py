# Date de antrenare generate automat

TRAINING_DATA = [
    ("Cum ud orhidee", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud orhideea", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Când trebuie să ud orhidee", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud orhideea", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Ce frecvență de udare are orhidee", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are orhideea", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Cât de des ud orhidee", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud orhideea", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la orhidee", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la orhideea", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Câtă lumină necesită orhidee", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită orhideea", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru orhidee", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru orhideea", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("orhidee are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("orhideea are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru orhidee", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru orhideea", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru orhidee", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru orhideea", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Când schimb substratul la orhidee", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la orhideea", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la orhidee", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la orhideea", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("orhidee are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("orhideea are frunze galbene", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("De ce are orhidee frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are orhideea frunze galbene", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("frunze galbene la orhidee", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la orhideea", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la orhidee", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la orhideea", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("orhidee are radacini putrede", {
        "entities": [(0, 7, 'PLANT'), (12, 28, 'PROBLEM')]
    }),
    ("orhideea are radacini putrede", {
        "entities": [(0, 8, 'PLANT'), (13, 29, 'PROBLEM')]
    }),
    ("De ce are orhidee radacini putrede", {
        "entities": [(10, 17, 'PLANT'), (18, 34, 'PROBLEM')]
    }),
    ("De ce are orhideea radacini putrede", {
        "entities": [(10, 18, 'PLANT'), (19, 35, 'PROBLEM')]
    }),
    ("radacini putrede la orhidee", {
        "entities": [(0, 16, 'PROBLEM'), (20, 27, 'PLANT')]
    }),
    ("radacini putrede la orhideea", {
        "entities": [(0, 16, 'PROBLEM'), (20, 28, 'PLANT')]
    }),
    ("Probleme cu radacini putrede la orhidee", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Probleme cu radacini putrede la orhideea", {
        "entities": [(12, 28, 'PROBLEM'), (32, 40, 'PLANT')]
    }),
    ("Cum ud ficus", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Cum ud ficusul", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud ficusului", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Când trebuie să ud ficus", {
        "entities": [(19, 24, 'PLANT')]
    }),
    ("Când trebuie să ud ficusul", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud ficusului", {
        "entities": [(19, 28, 'PLANT')]
    }),
    ("Ce frecvență de udare are ficus", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 31, 'PLANT')]
    }),
    ("Ce frecvență de udare are ficusul", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are ficusului", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 35, 'PLANT')]
    }),
    ("Cât de des ud ficus", {
        "entities": [(14, 19, 'PLANT')]
    }),
    ("Cât de des ud ficusul", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud ficusului", {
        "entities": [(14, 23, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la ficus", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 29, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la ficusul", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la ficusului", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 33, 'PLANT')]
    }),
    ("Câtă lumină necesită ficus", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 26, 'PLANT')]
    }),
    ("Câtă lumină necesită ficusul", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită ficusului", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 30, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru ficus", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 42, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru ficusul", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru ficusului", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 46, 'PLANT')]
    }),
    ("ficus are nevoie de lumină", {
        "entities": [(0, 5, 'PLANT'), (20, 26, 'CARE_ASPECT')]
    }),
    ("ficusul are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("ficusului are nevoie de lumină", {
        "entities": [(0, 9, 'PLANT'), (24, 30, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru ficus", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 33, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru ficusul", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru ficusului", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 37, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru ficus", {
        "entities": [(34, 39, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru ficusul", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru ficusului", {
        "entities": [(34, 43, 'PLANT')]
    }),
    ("Când schimb substratul la ficus", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Când schimb substratul la ficusul", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la ficusului", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la ficus", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la ficusul", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la ficusului", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 38, 'PLANT')]
    }),
    ("ficus are cadere frunze", {
        "entities": [(0, 5, 'PLANT'), (10, 23, 'PROBLEM')]
    }),
    ("ficusul are cadere frunze", {
        "entities": [(0, 7, 'PLANT'), (12, 25, 'PROBLEM')]
    }),
    ("ficusului are cadere frunze", {
        "entities": [(0, 9, 'PLANT'), (14, 27, 'PROBLEM')]
    }),
    ("De ce are ficus cadere frunze", {
        "entities": [(10, 15, 'PLANT'), (16, 29, 'PROBLEM')]
    }),
    ("De ce are ficusul cadere frunze", {
        "entities": [(10, 17, 'PLANT'), (18, 31, 'PROBLEM')]
    }),
    ("De ce are ficusului cadere frunze", {
        "entities": [(10, 19, 'PLANT'), (20, 33, 'PROBLEM')]
    }),
    ("cadere frunze la ficus", {
        "entities": [(0, 13, 'PROBLEM'), (17, 22, 'PLANT')]
    }),
    ("cadere frunze la ficusul", {
        "entities": [(0, 13, 'PROBLEM'), (17, 24, 'PLANT')]
    }),
    ("cadere frunze la ficusului", {
        "entities": [(0, 13, 'PROBLEM'), (17, 26, 'PLANT')]
    }),
    ("Probleme cu cadere frunze la ficus", {
        "entities": [(12, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Probleme cu cadere frunze la ficusul", {
        "entities": [(12, 25, 'PROBLEM'), (29, 36, 'PLANT')]
    }),
    ("Probleme cu cadere frunze la ficusului", {
        "entities": [(12, 25, 'PROBLEM'), (29, 38, 'PLANT')]
    }),
    ("ficus are frunze galbene", {
        "entities": [(0, 5, 'PLANT'), (10, 24, 'PROBLEM')]
    }),
    ("ficusul are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("ficusului are frunze galbene", {
        "entities": [(0, 9, 'PLANT'), (14, 28, 'PROBLEM')]
    }),
    ("De ce are ficus frunze galbene", {
        "entities": [(10, 15, 'PLANT'), (16, 30, 'PROBLEM')]
    }),
    ("De ce are ficusul frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are ficusului frunze galbene", {
        "entities": [(10, 19, 'PLANT'), (20, 34, 'PROBLEM')]
    }),
    ("frunze galbene la ficus", {
        "entities": [(0, 14, 'PROBLEM'), (18, 23, 'PLANT')]
    }),
    ("frunze galbene la ficusul", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la ficusului", {
        "entities": [(0, 14, 'PROBLEM'), (18, 27, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la ficus", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la ficusul", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la ficusului", {
        "entities": [(12, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Cum ud trandafir", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Cum ud trandafirul", {
        "entities": [(7, 18, 'PLANT')]
    }),
    ("Cum ud trandafirului", {
        "entities": [(7, 20, 'PLANT')]
    }),
    ("Când trebuie să ud trandafir", {
        "entities": [(19, 28, 'PLANT')]
    }),
    ("Când trebuie să ud trandafirul", {
        "entities": [(19, 30, 'PLANT')]
    }),
    ("Când trebuie să ud trandafirului", {
        "entities": [(19, 32, 'PLANT')]
    }),
    ("Ce frecvență de udare are trandafir", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 35, 'PLANT')]
    }),
    ("Ce frecvență de udare are trandafirul", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 37, 'PLANT')]
    }),
    ("Ce frecvență de udare are trandafirului", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 39, 'PLANT')]
    }),
    ("Cât de des ud trandafir", {
        "entities": [(14, 23, 'PLANT')]
    }),
    ("Cât de des ud trandafirul", {
        "entities": [(14, 25, 'PLANT')]
    }),
    ("Cât de des ud trandafirului", {
        "entities": [(14, 27, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la trandafir", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 33, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la trandafirul", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 35, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la trandafirului", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 37, 'PLANT')]
    }),
    ("Câtă lumină necesită trandafir", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 30, 'PLANT')]
    }),
    ("Câtă lumină necesită trandafirul", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 32, 'PLANT')]
    }),
    ("Câtă lumină necesită trandafirului", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 34, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru trandafir", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 46, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru trandafirul", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 48, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru trandafirului", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 50, 'PLANT')]
    }),
    ("trandafir are nevoie de lumină", {
        "entities": [(0, 9, 'PLANT'), (24, 30, 'CARE_ASPECT')]
    }),
    ("trandafirul are nevoie de lumină", {
        "entities": [(0, 11, 'PLANT'), (26, 32, 'CARE_ASPECT')]
    }),
    ("trandafirului are nevoie de lumină", {
        "entities": [(0, 13, 'PLANT'), (28, 34, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru trandafir", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 37, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru trandafirul", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 39, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru trandafirului", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru trandafir", {
        "entities": [(34, 43, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru trandafirul", {
        "entities": [(34, 45, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru trandafirului", {
        "entities": [(34, 47, 'PLANT')]
    }),
    ("Când schimb substratul la trandafir", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Când schimb substratul la trandafirul", {
        "entities": [(26, 37, 'PLANT')]
    }),
    ("Când schimb substratul la trandafirului", {
        "entities": [(26, 39, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la trandafir", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 38, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la trandafirul", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 40, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la trandafirului", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 42, 'PLANT')]
    }),
    ("trandafir are frunze galbene", {
        "entities": [(0, 9, 'PLANT'), (14, 28, 'PROBLEM')]
    }),
    ("trandafirul are frunze galbene", {
        "entities": [(0, 11, 'PLANT'), (16, 30, 'PROBLEM')]
    }),
    ("trandafirului are frunze galbene", {
        "entities": [(0, 13, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are trandafir frunze galbene", {
        "entities": [(10, 19, 'PLANT'), (20, 34, 'PROBLEM')]
    }),
    ("De ce are trandafirul frunze galbene", {
        "entities": [(10, 21, 'PLANT'), (22, 36, 'PROBLEM')]
    }),
    ("De ce are trandafirului frunze galbene", {
        "entities": [(10, 23, 'PLANT'), (24, 38, 'PROBLEM')]
    }),
    ("frunze galbene la trandafir", {
        "entities": [(0, 14, 'PROBLEM'), (18, 27, 'PLANT')]
    }),
    ("frunze galbene la trandafirul", {
        "entities": [(0, 14, 'PROBLEM'), (18, 29, 'PLANT')]
    }),
    ("frunze galbene la trandafirului", {
        "entities": [(0, 14, 'PROBLEM'), (18, 31, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la trandafir", {
        "entities": [(12, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la trandafirul", {
        "entities": [(12, 26, 'PROBLEM'), (30, 41, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la trandafirului", {
        "entities": [(12, 26, 'PROBLEM'), (30, 43, 'PLANT')]
    }),
    ("trandafir are pete negre", {
        "entities": [(0, 9, 'PLANT'), (14, 24, 'PROBLEM')]
    }),
    ("trandafirul are pete negre", {
        "entities": [(0, 11, 'PLANT'), (16, 26, 'PROBLEM')]
    }),
    ("trandafirului are pete negre", {
        "entities": [(0, 13, 'PLANT'), (18, 28, 'PROBLEM')]
    }),
    ("De ce are trandafir pete negre", {
        "entities": [(10, 19, 'PLANT'), (20, 30, 'PROBLEM')]
    }),
    ("De ce are trandafirul pete negre", {
        "entities": [(10, 21, 'PLANT'), (22, 32, 'PROBLEM')]
    }),
    ("De ce are trandafirului pete negre", {
        "entities": [(10, 23, 'PLANT'), (24, 34, 'PROBLEM')]
    }),
    ("pete negre la trandafir", {
        "entities": [(0, 10, 'PROBLEM'), (14, 23, 'PLANT')]
    }),
    ("pete negre la trandafirul", {
        "entities": [(0, 10, 'PROBLEM'), (14, 25, 'PLANT')]
    }),
    ("pete negre la trandafirului", {
        "entities": [(0, 10, 'PROBLEM'), (14, 27, 'PLANT')]
    }),
    ("Probleme cu pete negre la trandafir", {
        "entities": [(12, 22, 'PROBLEM'), (26, 35, 'PLANT')]
    }),
    ("Probleme cu pete negre la trandafirul", {
        "entities": [(12, 22, 'PROBLEM'), (26, 37, 'PLANT')]
    }),
    ("Probleme cu pete negre la trandafirului", {
        "entities": [(12, 22, 'PROBLEM'), (26, 39, 'PLANT')]
    }),
    ("Cum ud crin", {
        "entities": [(7, 11, 'PLANT')]
    }),
    ("Cum ud crinul", {
        "entities": [(7, 13, 'PLANT')]
    }),
    ("Cum ud crinului", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Când trebuie să ud crin", {
        "entities": [(19, 23, 'PLANT')]
    }),
    ("Când trebuie să ud crinul", {
        "entities": [(19, 25, 'PLANT')]
    }),
    ("Când trebuie să ud crinului", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Ce frecvență de udare are crin", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 30, 'PLANT')]
    }),
    ("Ce frecvență de udare are crinul", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 32, 'PLANT')]
    }),
    ("Ce frecvență de udare are crinului", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Cât de des ud crin", {
        "entities": [(14, 18, 'PLANT')]
    }),
    ("Cât de des ud crinul", {
        "entities": [(14, 20, 'PLANT')]
    }),
    ("Cât de des ud crinului", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la crin", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 28, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la crinul", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 30, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la crinului", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Câtă lumină necesită crin", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 25, 'PLANT')]
    }),
    ("Câtă lumină necesită crinul", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 27, 'PLANT')]
    }),
    ("Câtă lumină necesită crinului", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru crin", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 41, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru crinul", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 43, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru crinului", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("crin are nevoie de lumină", {
        "entities": [(0, 4, 'PLANT'), (19, 25, 'CARE_ASPECT')]
    }),
    ("crinul are nevoie de lumină", {
        "entities": [(0, 6, 'PLANT'), (21, 27, 'CARE_ASPECT')]
    }),
    ("crinului are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru crin", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 32, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru crinul", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 34, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru crinului", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru crin", {
        "entities": [(34, 38, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru crinul", {
        "entities": [(34, 40, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru crinului", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Când schimb substratul la crin", {
        "entities": [(26, 30, 'PLANT')]
    }),
    ("Când schimb substratul la crinul", {
        "entities": [(26, 32, 'PLANT')]
    }),
    ("Când schimb substratul la crinului", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la crin", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 33, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la crinul", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 35, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la crinului", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("crin are ingalbenirea frunzelor", {
        "entities": [(0, 4, 'PLANT'), (9, 31, 'PROBLEM')]
    }),
    ("crinul are ingalbenirea frunzelor", {
        "entities": [(0, 6, 'PLANT'), (11, 33, 'PROBLEM')]
    }),
    ("crinului are ingalbenirea frunzelor", {
        "entities": [(0, 8, 'PLANT'), (13, 35, 'PROBLEM')]
    }),
    ("De ce are crin ingalbenirea frunzelor", {
        "entities": [(10, 14, 'PLANT'), (15, 37, 'PROBLEM')]
    }),
    ("De ce are crinul ingalbenirea frunzelor", {
        "entities": [(10, 16, 'PLANT'), (17, 39, 'PROBLEM')]
    }),
    ("De ce are crinului ingalbenirea frunzelor", {
        "entities": [(10, 18, 'PLANT'), (19, 41, 'PROBLEM')]
    }),
    ("ingalbenirea frunzelor la crin", {
        "entities": [(0, 22, 'PROBLEM'), (26, 30, 'PLANT')]
    }),
    ("ingalbenirea frunzelor la crinul", {
        "entities": [(0, 22, 'PROBLEM'), (26, 32, 'PLANT')]
    }),
    ("ingalbenirea frunzelor la crinului", {
        "entities": [(0, 22, 'PROBLEM'), (26, 34, 'PLANT')]
    }),
    ("Probleme cu ingalbenirea frunzelor la crin", {
        "entities": [(12, 34, 'PROBLEM'), (38, 42, 'PLANT')]
    }),
    ("Probleme cu ingalbenirea frunzelor la crinul", {
        "entities": [(12, 34, 'PROBLEM'), (38, 44, 'PLANT')]
    }),
    ("Probleme cu ingalbenirea frunzelor la crinului", {
        "entities": [(12, 34, 'PROBLEM'), (38, 46, 'PLANT')]
    }),
    ("crin are lipsa inflorire", {
        "entities": [(0, 4, 'PLANT'), (9, 24, 'PROBLEM')]
    }),
    ("crinul are lipsa inflorire", {
        "entities": [(0, 6, 'PLANT'), (11, 26, 'PROBLEM')]
    }),
    ("crinului are lipsa inflorire", {
        "entities": [(0, 8, 'PLANT'), (13, 28, 'PROBLEM')]
    }),
    ("De ce are crin lipsa inflorire", {
        "entities": [(10, 14, 'PLANT'), (15, 30, 'PROBLEM')]
    }),
    ("De ce are crinul lipsa inflorire", {
        "entities": [(10, 16, 'PLANT'), (17, 32, 'PROBLEM')]
    }),
    ("De ce are crinului lipsa inflorire", {
        "entities": [(10, 18, 'PLANT'), (19, 34, 'PROBLEM')]
    }),
    ("lipsa inflorire la crin", {
        "entities": [(0, 15, 'PROBLEM'), (19, 23, 'PLANT')]
    }),
    ("lipsa inflorire la crinul", {
        "entities": [(0, 15, 'PROBLEM'), (19, 25, 'PLANT')]
    }),
    ("lipsa inflorire la crinului", {
        "entities": [(0, 15, 'PROBLEM'), (19, 27, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la crin", {
        "entities": [(12, 27, 'PROBLEM'), (31, 35, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la crinul", {
        "entities": [(12, 27, 'PROBLEM'), (31, 37, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la crinului", {
        "entities": [(12, 27, 'PROBLEM'), (31, 39, 'PLANT')]
    }),
    ("Cum ud muscata", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud muscataul", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Cum ud muscataului", {
        "entities": [(7, 18, 'PLANT')]
    }),
    ("Când trebuie să ud muscata", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud muscataul", {
        "entities": [(19, 28, 'PLANT')]
    }),
    ("Când trebuie să ud muscataului", {
        "entities": [(19, 30, 'PLANT')]
    }),
    ("Ce frecvență de udare are muscata", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are muscataul", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 35, 'PLANT')]
    }),
    ("Ce frecvență de udare are muscataului", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 37, 'PLANT')]
    }),
    ("Cât de des ud muscata", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud muscataul", {
        "entities": [(14, 23, 'PLANT')]
    }),
    ("Cât de des ud muscataului", {
        "entities": [(14, 25, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la muscata", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la muscataul", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 33, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la muscataului", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 35, 'PLANT')]
    }),
    ("Câtă lumină necesită muscata", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită muscataul", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 30, 'PLANT')]
    }),
    ("Câtă lumină necesită muscataului", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 32, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru muscata", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru muscataul", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 46, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru muscataului", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 48, 'PLANT')]
    }),
    ("muscata are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("muscataul are nevoie de lumină", {
        "entities": [(0, 9, 'PLANT'), (24, 30, 'CARE_ASPECT')]
    }),
    ("muscataului are nevoie de lumină", {
        "entities": [(0, 11, 'PLANT'), (26, 32, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru muscata", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru muscataul", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 37, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru muscataului", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 39, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru muscata", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru muscataul", {
        "entities": [(34, 43, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru muscataului", {
        "entities": [(34, 45, 'PLANT')]
    }),
    ("Când schimb substratul la muscata", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la muscataul", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Când schimb substratul la muscataului", {
        "entities": [(26, 37, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la muscata", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la muscataul", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 38, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la muscataului", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 40, 'PLANT')]
    }),
    ("muscata are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("muscataul are frunze galbene", {
        "entities": [(0, 9, 'PLANT'), (14, 28, 'PROBLEM')]
    }),
    ("muscataului are frunze galbene", {
        "entities": [(0, 11, 'PLANT'), (16, 30, 'PROBLEM')]
    }),
    ("De ce are muscata frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are muscataul frunze galbene", {
        "entities": [(10, 19, 'PLANT'), (20, 34, 'PROBLEM')]
    }),
    ("De ce are muscataului frunze galbene", {
        "entities": [(10, 21, 'PLANT'), (22, 36, 'PROBLEM')]
    }),
    ("frunze galbene la muscata", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la muscataul", {
        "entities": [(0, 14, 'PROBLEM'), (18, 27, 'PLANT')]
    }),
    ("frunze galbene la muscataului", {
        "entities": [(0, 14, 'PROBLEM'), (18, 29, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la muscata", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la muscataul", {
        "entities": [(12, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la muscataului", {
        "entities": [(12, 26, 'PROBLEM'), (30, 41, 'PLANT')]
    }),
    ("muscata are putine flori", {
        "entities": [(0, 7, 'PLANT'), (12, 24, 'PROBLEM')]
    }),
    ("muscataul are putine flori", {
        "entities": [(0, 9, 'PLANT'), (14, 26, 'PROBLEM')]
    }),
    ("muscataului are putine flori", {
        "entities": [(0, 11, 'PLANT'), (16, 28, 'PROBLEM')]
    }),
    ("De ce are muscata putine flori", {
        "entities": [(10, 17, 'PLANT'), (18, 30, 'PROBLEM')]
    }),
    ("De ce are muscataul putine flori", {
        "entities": [(10, 19, 'PLANT'), (20, 32, 'PROBLEM')]
    }),
    ("De ce are muscataului putine flori", {
        "entities": [(10, 21, 'PLANT'), (22, 34, 'PROBLEM')]
    }),
    ("putine flori la muscata", {
        "entities": [(0, 12, 'PROBLEM'), (16, 23, 'PLANT')]
    }),
    ("putine flori la muscataul", {
        "entities": [(0, 12, 'PROBLEM'), (16, 25, 'PLANT')]
    }),
    ("putine flori la muscataului", {
        "entities": [(0, 12, 'PROBLEM'), (16, 27, 'PLANT')]
    }),
    ("Probleme cu putine flori la muscata", {
        "entities": [(12, 24, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Probleme cu putine flori la muscataul", {
        "entities": [(12, 24, 'PROBLEM'), (28, 37, 'PLANT')]
    }),
    ("Probleme cu putine flori la muscataului", {
        "entities": [(12, 24, 'PROBLEM'), (28, 39, 'PLANT')]
    }),
    ("Nu știu ce să fac", {
        "entities": []
    }),
    ("Care sunt pașii de îngrijire", {
        "entities": []
    }),
    ("Am nevoie de ajutor", {
        "entities": []
    }),
    ("Planta mea nu arată bine", {
        "entities": []
    }),
    ("Ce să fac mai departe", {
        "entities": []
    }),
    ("Cum procedez", {
        "entities": []
    }),
]

# Lista de entitati cunoscute
ENTITIES = {
    "PLANT": ['orhidee', 'orhideea', 'ficus', 'ficusul', 'ficusului', 'trandafir', 'trandafirul', 'trandafirului', 'crin', 'crinul', 'crinului', 'muscata', 'muscataul', 'muscataului'],
    "CARE_ASPECT": ['udare', 'lumina', 'substrat', 'lumină', 'pământ', 'sol'],
    "PROBLEM": ['frunze galbene', 'radacini putrede', 'cadere frunze', 'frunze galbene', 'frunze galbene', 'pete negre', 'ingalbenirea frunzelor', 'lipsa inflorire', 'frunze galbene', 'putine flori']
}