# Date de antrenare generate automat

TRAINING_DATA = [
    ("Cum ud orhidee", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud orhidea", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud orhideei", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Când trebuie să ud orhidee", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud orhidea", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud orhideei", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Ce frecvență de udare are orhidee", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are orhidea", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are orhideei", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Cât de des ud orhidee", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud orhidea", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud orhideei", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la orhidee", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la orhidea", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la orhideei", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Câtă lumină necesită orhidee", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită orhidea", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită orhideei", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru orhidee", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru orhidea", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru orhideei", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("orhidee are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("orhidea are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("orhideei are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru orhidee", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru orhidea", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru orhideei", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru orhidee", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru orhidea", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru orhideei", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Când schimb substratul la orhidee", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la orhidea", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la orhideei", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la orhidee", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la orhidea", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la orhideei", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("orhidee are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("orhidea are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("orhideei are frunze galbene", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("De ce are orhidee frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are orhidea frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are orhideei frunze galbene", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("frunze galbene la orhidee", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la orhidea", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la orhideei", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la orhidee", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la orhidea", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la orhideei", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("orhidee are radacini putrede", {
        "entities": [(0, 7, 'PLANT'), (12, 28, 'PROBLEM')]
    }),
    ("orhidea are radacini putrede", {
        "entities": [(0, 7, 'PLANT'), (12, 28, 'PROBLEM')]
    }),
    ("orhideei are radacini putrede", {
        "entities": [(0, 8, 'PLANT'), (13, 29, 'PROBLEM')]
    }),
    ("De ce are orhidee radacini putrede", {
        "entities": [(10, 17, 'PLANT'), (18, 34, 'PROBLEM')]
    }),
    ("De ce are orhidea radacini putrede", {
        "entities": [(10, 17, 'PLANT'), (18, 34, 'PROBLEM')]
    }),
    ("De ce are orhideei radacini putrede", {
        "entities": [(10, 18, 'PLANT'), (19, 35, 'PROBLEM')]
    }),
    ("radacini putrede la orhidee", {
        "entities": [(0, 16, 'PROBLEM'), (20, 27, 'PLANT')]
    }),
    ("radacini putrede la orhidea", {
        "entities": [(0, 16, 'PROBLEM'), (20, 27, 'PLANT')]
    }),
    ("radacini putrede la orhideei", {
        "entities": [(0, 16, 'PROBLEM'), (20, 28, 'PLANT')]
    }),
    ("Probleme cu radacini putrede la orhidee", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Probleme cu radacini putrede la orhidea", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Probleme cu radacini putrede la orhideei", {
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
    ("Cum ud muscata", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud muscatei", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Când trebuie să ud muscata", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud muscata", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud muscatei", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Ce frecvență de udare are muscata", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are muscata", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are muscatei", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Cât de des ud muscata", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud muscata", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud muscatei", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la muscata", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la muscata", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la muscatei", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Câtă lumină necesită muscata", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită muscata", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită muscatei", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru muscata", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru muscata", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru muscatei", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("muscata are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("muscata are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("muscatei are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru muscata", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru muscata", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru muscatei", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru muscata", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru muscata", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru muscatei", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Când schimb substratul la muscata", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la muscata", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la muscatei", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la muscata", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la muscata", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la muscatei", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("muscata are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("muscata are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("muscatei are frunze galbene", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("De ce are muscata frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are muscata frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are muscatei frunze galbene", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("frunze galbene la muscata", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la muscata", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la muscatei", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la muscata", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la muscata", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la muscatei", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("muscata are putine flori", {
        "entities": [(0, 7, 'PLANT'), (12, 24, 'PROBLEM')]
    }),
    ("muscata are putine flori", {
        "entities": [(0, 7, 'PLANT'), (12, 24, 'PROBLEM')]
    }),
    ("muscatei are putine flori", {
        "entities": [(0, 8, 'PLANT'), (13, 25, 'PROBLEM')]
    }),
    ("De ce are muscata putine flori", {
        "entities": [(10, 17, 'PLANT'), (18, 30, 'PROBLEM')]
    }),
    ("De ce are muscata putine flori", {
        "entities": [(10, 17, 'PLANT'), (18, 30, 'PROBLEM')]
    }),
    ("De ce are muscatei putine flori", {
        "entities": [(10, 18, 'PLANT'), (19, 31, 'PROBLEM')]
    }),
    ("putine flori la muscata", {
        "entities": [(0, 12, 'PROBLEM'), (16, 23, 'PLANT')]
    }),
    ("putine flori la muscata", {
        "entities": [(0, 12, 'PROBLEM'), (16, 23, 'PLANT')]
    }),
    ("putine flori la muscatei", {
        "entities": [(0, 12, 'PROBLEM'), (16, 24, 'PLANT')]
    }),
    ("Probleme cu putine flori la muscata", {
        "entities": [(12, 24, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Probleme cu putine flori la muscata", {
        "entities": [(12, 24, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Probleme cu putine flori la muscatei", {
        "entities": [(12, 24, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("Cum ud aloe vera", {
        "entities": []
    }),
    ("Cum ud aloe vera", {
        "entities": []
    }),
    ("Cum ud aloe verei", {
        "entities": []
    }),
    ("Când trebuie să ud aloe vera", {
        "entities": []
    }),
    ("Când trebuie să ud aloe vera", {
        "entities": []
    }),
    ("Când trebuie să ud aloe verei", {
        "entities": []
    }),
    ("Ce frecvență de udare are aloe vera", {
        "entities": [(16, 21, 'CARE_ASPECT')]
    }),
    ("Ce frecvență de udare are aloe vera", {
        "entities": [(16, 21, 'CARE_ASPECT')]
    }),
    ("Ce frecvență de udare are aloe verei", {
        "entities": [(16, 21, 'CARE_ASPECT')]
    }),
    ("Cât de des ud aloe vera", {
        "entities": []
    }),
    ("Cât de des ud aloe vera", {
        "entities": []
    }),
    ("Cât de des ud aloe verei", {
        "entities": []
    }),
    ("Ce lumină îi trebuie la aloe vera", {
        "entities": [(3, 9, 'CARE_ASPECT')]
    }),
    ("Ce lumină îi trebuie la aloe vera", {
        "entities": [(3, 9, 'CARE_ASPECT')]
    }),
    ("Ce lumină îi trebuie la aloe verei", {
        "entities": [(3, 9, 'CARE_ASPECT')]
    }),
    ("Câtă lumină necesită aloe vera", {
        "entities": [(5, 11, 'CARE_ASPECT')]
    }),
    ("Câtă lumină necesită aloe vera", {
        "entities": [(5, 11, 'CARE_ASPECT')]
    }),
    ("Câtă lumină necesită aloe verei", {
        "entities": [(5, 11, 'CARE_ASPECT')]
    }),
    ("Care sunt cerințele de lumină pentru aloe vera", {
        "entities": [(23, 29, 'CARE_ASPECT')]
    }),
    ("Care sunt cerințele de lumină pentru aloe vera", {
        "entities": [(23, 29, 'CARE_ASPECT')]
    }),
    ("Care sunt cerințele de lumină pentru aloe verei", {
        "entities": [(23, 29, 'CARE_ASPECT')]
    }),
    ("aloe vera are nevoie de lumină", {
        "entities": [(24, 30, 'CARE_ASPECT')]
    }),
    ("aloe vera are nevoie de lumină", {
        "entities": [(24, 30, 'CARE_ASPECT')]
    }),
    ("aloe verei are nevoie de lumină", {
        "entities": [(25, 31, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru aloe vera", {
        "entities": [(3, 11, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru aloe vera", {
        "entities": [(3, 11, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru aloe verei", {
        "entities": [(3, 11, 'CARE_ASPECT')]
    }),
    ("Care e substratul potrivit pentru aloe vera", {
        "entities": []
    }),
    ("Care e substratul potrivit pentru aloe vera", {
        "entities": []
    }),
    ("Care e substratul potrivit pentru aloe verei", {
        "entities": []
    }),
    ("Când schimb substratul la aloe vera", {
        "entities": []
    }),
    ("Când schimb substratul la aloe vera", {
        "entities": []
    }),
    ("Când schimb substratul la aloe verei", {
        "entities": []
    }),
    ("Ce tip de pământ folosesc la aloe vera", {
        "entities": [(10, 16, 'CARE_ASPECT')]
    }),
    ("Ce tip de pământ folosesc la aloe vera", {
        "entities": [(10, 16, 'CARE_ASPECT')]
    }),
    ("Ce tip de pământ folosesc la aloe verei", {
        "entities": [(10, 16, 'CARE_ASPECT')]
    }),
    ("aloe vera are frunze maro", {
        "entities": [(14, 25, 'PROBLEM')]
    }),
    ("aloe vera are frunze maro", {
        "entities": [(14, 25, 'PROBLEM')]
    }),
    ("aloe verei are frunze maro", {
        "entities": [(15, 26, 'PROBLEM')]
    }),
    ("De ce are aloe vera frunze maro", {
        "entities": [(20, 31, 'PROBLEM')]
    }),
    ("De ce are aloe vera frunze maro", {
        "entities": [(20, 31, 'PROBLEM')]
    }),
    ("De ce are aloe verei frunze maro", {
        "entities": [(21, 32, 'PROBLEM')]
    }),
    ("frunze maro la aloe vera", {
        "entities": [(0, 11, 'PROBLEM')]
    }),
    ("frunze maro la aloe vera", {
        "entities": [(0, 11, 'PROBLEM')]
    }),
    ("frunze maro la aloe verei", {
        "entities": [(0, 11, 'PROBLEM')]
    }),
    ("Probleme cu frunze maro la aloe vera", {
        "entities": [(12, 23, 'PROBLEM')]
    }),
    ("Probleme cu frunze maro la aloe vera", {
        "entities": [(12, 23, 'PROBLEM')]
    }),
    ("Probleme cu frunze maro la aloe verei", {
        "entities": [(12, 23, 'PROBLEM')]
    }),
    ("aloe vera are frunze moi", {
        "entities": [(14, 24, 'PROBLEM')]
    }),
    ("aloe vera are frunze moi", {
        "entities": [(14, 24, 'PROBLEM')]
    }),
    ("aloe verei are frunze moi", {
        "entities": [(15, 25, 'PROBLEM')]
    }),
    ("De ce are aloe vera frunze moi", {
        "entities": [(20, 30, 'PROBLEM')]
    }),
    ("De ce are aloe vera frunze moi", {
        "entities": [(20, 30, 'PROBLEM')]
    }),
    ("De ce are aloe verei frunze moi", {
        "entities": [(21, 31, 'PROBLEM')]
    }),
    ("frunze moi la aloe vera", {
        "entities": [(0, 10, 'PROBLEM')]
    }),
    ("frunze moi la aloe vera", {
        "entities": [(0, 10, 'PROBLEM')]
    }),
    ("frunze moi la aloe verei", {
        "entities": [(0, 10, 'PROBLEM')]
    }),
    ("Probleme cu frunze moi la aloe vera", {
        "entities": [(12, 22, 'PROBLEM')]
    }),
    ("Probleme cu frunze moi la aloe vera", {
        "entities": [(12, 22, 'PROBLEM')]
    }),
    ("Probleme cu frunze moi la aloe verei", {
        "entities": [(12, 22, 'PROBLEM')]
    }),
    ("aloe vera are putrezirea bazei", {
        "entities": [(14, 30, 'PROBLEM')]
    }),
    ("aloe vera are putrezirea bazei", {
        "entities": [(14, 30, 'PROBLEM')]
    }),
    ("aloe verei are putrezirea bazei", {
        "entities": [(15, 31, 'PROBLEM')]
    }),
    ("De ce are aloe vera putrezirea bazei", {
        "entities": [(20, 36, 'PROBLEM')]
    }),
    ("De ce are aloe vera putrezirea bazei", {
        "entities": [(20, 36, 'PROBLEM')]
    }),
    ("De ce are aloe verei putrezirea bazei", {
        "entities": [(21, 37, 'PROBLEM')]
    }),
    ("putrezirea bazei la aloe vera", {
        "entities": [(0, 16, 'PROBLEM')]
    }),
    ("putrezirea bazei la aloe vera", {
        "entities": [(0, 16, 'PROBLEM')]
    }),
    ("putrezirea bazei la aloe verei", {
        "entities": [(0, 16, 'PROBLEM')]
    }),
    ("Probleme cu putrezirea bazei la aloe vera", {
        "entities": [(12, 28, 'PROBLEM')]
    }),
    ("Probleme cu putrezirea bazei la aloe vera", {
        "entities": [(12, 28, 'PROBLEM')]
    }),
    ("Probleme cu putrezirea bazei la aloe verei", {
        "entities": [(12, 28, 'PROBLEM')]
    }),
    ("Cum ud cactus", {
        "entities": [(7, 13, 'PLANT')]
    }),
    ("Cum ud cactusul", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Cum ud cactusului", {
        "entities": [(7, 17, 'PLANT')]
    }),
    ("Când trebuie să ud cactus", {
        "entities": [(19, 25, 'PLANT')]
    }),
    ("Când trebuie să ud cactusul", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Când trebuie să ud cactusului", {
        "entities": [(19, 29, 'PLANT')]
    }),
    ("Ce frecvență de udare are cactus", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 32, 'PLANT')]
    }),
    ("Ce frecvență de udare are cactusul", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Ce frecvență de udare are cactusului", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 36, 'PLANT')]
    }),
    ("Cât de des ud cactus", {
        "entities": [(14, 20, 'PLANT')]
    }),
    ("Cât de des ud cactusul", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Cât de des ud cactusului", {
        "entities": [(14, 24, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la cactus", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 30, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la cactusul", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la cactusului", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 34, 'PLANT')]
    }),
    ("Câtă lumină necesită cactus", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 27, 'PLANT')]
    }),
    ("Câtă lumină necesită cactusul", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Câtă lumină necesită cactusului", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 31, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru cactus", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 43, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru cactusul", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru cactusului", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 47, 'PLANT')]
    }),
    ("cactus are nevoie de lumină", {
        "entities": [(0, 6, 'PLANT'), (21, 27, 'CARE_ASPECT')]
    }),
    ("cactusul are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("cactusului are nevoie de lumină", {
        "entities": [(0, 10, 'PLANT'), (25, 31, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru cactus", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 34, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru cactusul", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru cactusului", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 38, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru cactus", {
        "entities": [(34, 40, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru cactusul", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru cactusului", {
        "entities": [(34, 44, 'PLANT')]
    }),
    ("Când schimb substratul la cactus", {
        "entities": [(26, 32, 'PLANT')]
    }),
    ("Când schimb substratul la cactusul", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Când schimb substratul la cactusului", {
        "entities": [(26, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la cactus", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 35, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la cactusul", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la cactusului", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 39, 'PLANT')]
    }),
    ("cactus are putrezire baza", {
        "entities": [(0, 6, 'PLANT'), (11, 25, 'PROBLEM')]
    }),
    ("cactusul are putrezire baza", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("cactusului are putrezire baza", {
        "entities": [(0, 10, 'PLANT'), (15, 29, 'PROBLEM')]
    }),
    ("De ce are cactus putrezire baza", {
        "entities": [(10, 16, 'PLANT'), (17, 31, 'PROBLEM')]
    }),
    ("De ce are cactusul putrezire baza", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("De ce are cactusului putrezire baza", {
        "entities": [(10, 20, 'PLANT'), (21, 35, 'PROBLEM')]
    }),
    ("putrezire baza la cactus", {
        "entities": [(0, 14, 'PROBLEM'), (18, 24, 'PLANT')]
    }),
    ("putrezire baza la cactusul", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("putrezire baza la cactusului", {
        "entities": [(0, 14, 'PROBLEM'), (18, 28, 'PLANT')]
    }),
    ("Probleme cu putrezire baza la cactus", {
        "entities": [(12, 26, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("Probleme cu putrezire baza la cactusul", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("Probleme cu putrezire baza la cactusului", {
        "entities": [(12, 26, 'PROBLEM'), (30, 40, 'PLANT')]
    }),
    ("cactus are crestere alungita", {
        "entities": [(0, 6, 'PLANT'), (11, 28, 'PROBLEM')]
    }),
    ("cactusul are crestere alungita", {
        "entities": [(0, 8, 'PLANT'), (13, 30, 'PROBLEM')]
    }),
    ("cactusului are crestere alungita", {
        "entities": [(0, 10, 'PLANT'), (15, 32, 'PROBLEM')]
    }),
    ("De ce are cactus crestere alungita", {
        "entities": [(10, 16, 'PLANT'), (17, 34, 'PROBLEM')]
    }),
    ("De ce are cactusul crestere alungita", {
        "entities": [(10, 18, 'PLANT'), (19, 36, 'PROBLEM')]
    }),
    ("De ce are cactusului crestere alungita", {
        "entities": [(10, 20, 'PLANT'), (21, 38, 'PROBLEM')]
    }),
    ("crestere alungita la cactus", {
        "entities": [(0, 17, 'PROBLEM'), (21, 27, 'PLANT')]
    }),
    ("crestere alungita la cactusul", {
        "entities": [(0, 17, 'PROBLEM'), (21, 29, 'PLANT')]
    }),
    ("crestere alungita la cactusului", {
        "entities": [(0, 17, 'PROBLEM'), (21, 31, 'PLANT')]
    }),
    ("Probleme cu crestere alungita la cactus", {
        "entities": [(12, 29, 'PROBLEM'), (33, 39, 'PLANT')]
    }),
    ("Probleme cu crestere alungita la cactusul", {
        "entities": [(12, 29, 'PROBLEM'), (33, 41, 'PLANT')]
    }),
    ("Probleme cu crestere alungita la cactusului", {
        "entities": [(12, 29, 'PROBLEM'), (33, 43, 'PLANT')]
    }),
    ("cactus are pete maronii", {
        "entities": [(0, 6, 'PLANT'), (11, 23, 'PROBLEM')]
    }),
    ("cactusul are pete maronii", {
        "entities": [(0, 8, 'PLANT'), (13, 25, 'PROBLEM')]
    }),
    ("cactusului are pete maronii", {
        "entities": [(0, 10, 'PLANT'), (15, 27, 'PROBLEM')]
    }),
    ("De ce are cactus pete maronii", {
        "entities": [(10, 16, 'PLANT'), (17, 29, 'PROBLEM')]
    }),
    ("De ce are cactusul pete maronii", {
        "entities": [(10, 18, 'PLANT'), (19, 31, 'PROBLEM')]
    }),
    ("De ce are cactusului pete maronii", {
        "entities": [(10, 20, 'PLANT'), (21, 33, 'PROBLEM')]
    }),
    ("pete maronii la cactus", {
        "entities": [(0, 12, 'PROBLEM'), (16, 22, 'PLANT')]
    }),
    ("pete maronii la cactusul", {
        "entities": [(0, 12, 'PROBLEM'), (16, 24, 'PLANT')]
    }),
    ("pete maronii la cactusului", {
        "entities": [(0, 12, 'PROBLEM'), (16, 26, 'PLANT')]
    }),
    ("Probleme cu pete maronii la cactus", {
        "entities": [(12, 24, 'PROBLEM'), (28, 34, 'PLANT')]
    }),
    ("Probleme cu pete maronii la cactusul", {
        "entities": [(12, 24, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("Probleme cu pete maronii la cactusului", {
        "entities": [(12, 24, 'PROBLEM'), (28, 38, 'PLANT')]
    }),
    ("Cum ud lavanda", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud lavanda", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud lavandei", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Când trebuie să ud lavanda", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud lavanda", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud lavandei", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Ce frecvență de udare are lavanda", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are lavanda", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are lavandei", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Cât de des ud lavanda", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud lavanda", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud lavandei", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la lavanda", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la lavanda", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la lavandei", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Câtă lumină necesită lavanda", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită lavanda", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită lavandei", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru lavanda", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru lavanda", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru lavandei", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("lavanda are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("lavanda are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("lavandei are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru lavanda", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru lavanda", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru lavandei", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru lavanda", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru lavanda", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru lavandei", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Când schimb substratul la lavanda", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la lavanda", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la lavandei", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la lavanda", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la lavanda", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la lavandei", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("lavanda are putrezire radacini", {
        "entities": [(0, 7, 'PLANT'), (12, 30, 'PROBLEM')]
    }),
    ("lavanda are putrezire radacini", {
        "entities": [(0, 7, 'PLANT'), (12, 30, 'PROBLEM')]
    }),
    ("lavandei are putrezire radacini", {
        "entities": [(0, 8, 'PLANT'), (13, 31, 'PROBLEM')]
    }),
    ("De ce are lavanda putrezire radacini", {
        "entities": [(10, 17, 'PLANT'), (18, 36, 'PROBLEM')]
    }),
    ("De ce are lavanda putrezire radacini", {
        "entities": [(10, 17, 'PLANT'), (18, 36, 'PROBLEM')]
    }),
    ("De ce are lavandei putrezire radacini", {
        "entities": [(10, 18, 'PLANT'), (19, 37, 'PROBLEM')]
    }),
    ("putrezire radacini la lavanda", {
        "entities": [(0, 18, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("putrezire radacini la lavanda", {
        "entities": [(0, 18, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("putrezire radacini la lavandei", {
        "entities": [(0, 18, 'PROBLEM'), (22, 30, 'PLANT')]
    }),
    ("Probleme cu putrezire radacini la lavanda", {
        "entities": [(12, 30, 'PROBLEM'), (34, 41, 'PLANT')]
    }),
    ("Probleme cu putrezire radacini la lavanda", {
        "entities": [(12, 30, 'PROBLEM'), (34, 41, 'PLANT')]
    }),
    ("Probleme cu putrezire radacini la lavandei", {
        "entities": [(12, 30, 'PROBLEM'), (34, 42, 'PLANT')]
    }),
    ("lavanda are crestere lemnoasa", {
        "entities": [(0, 7, 'PLANT'), (12, 29, 'PROBLEM')]
    }),
    ("lavanda are crestere lemnoasa", {
        "entities": [(0, 7, 'PLANT'), (12, 29, 'PROBLEM')]
    }),
    ("lavandei are crestere lemnoasa", {
        "entities": [(0, 8, 'PLANT'), (13, 30, 'PROBLEM')]
    }),
    ("De ce are lavanda crestere lemnoasa", {
        "entities": [(10, 17, 'PLANT'), (18, 35, 'PROBLEM')]
    }),
    ("De ce are lavanda crestere lemnoasa", {
        "entities": [(10, 17, 'PLANT'), (18, 35, 'PROBLEM')]
    }),
    ("De ce are lavandei crestere lemnoasa", {
        "entities": [(10, 18, 'PLANT'), (19, 36, 'PROBLEM')]
    }),
    ("crestere lemnoasa la lavanda", {
        "entities": [(0, 17, 'PROBLEM'), (21, 28, 'PLANT')]
    }),
    ("crestere lemnoasa la lavanda", {
        "entities": [(0, 17, 'PROBLEM'), (21, 28, 'PLANT')]
    }),
    ("crestere lemnoasa la lavandei", {
        "entities": [(0, 17, 'PROBLEM'), (21, 29, 'PLANT')]
    }),
    ("Probleme cu crestere lemnoasa la lavanda", {
        "entities": [(12, 29, 'PROBLEM'), (33, 40, 'PLANT')]
    }),
    ("Probleme cu crestere lemnoasa la lavanda", {
        "entities": [(12, 29, 'PROBLEM'), (33, 40, 'PLANT')]
    }),
    ("Probleme cu crestere lemnoasa la lavandei", {
        "entities": [(12, 29, 'PROBLEM'), (33, 41, 'PLANT')]
    }),
    ("lavanda are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("lavanda are frunze galbene", {
        "entities": [(0, 7, 'PLANT'), (12, 26, 'PROBLEM')]
    }),
    ("lavandei are frunze galbene", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("De ce are lavanda frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are lavanda frunze galbene", {
        "entities": [(10, 17, 'PLANT'), (18, 32, 'PROBLEM')]
    }),
    ("De ce are lavandei frunze galbene", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("frunze galbene la lavanda", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la lavanda", {
        "entities": [(0, 14, 'PROBLEM'), (18, 25, 'PLANT')]
    }),
    ("frunze galbene la lavandei", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la lavanda", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la lavanda", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la lavandei", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("Cum ud lalea", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Cum ud lalea", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Cum ud laleei", {
        "entities": [(7, 13, 'PLANT')]
    }),
    ("Când trebuie să ud lalea", {
        "entities": [(19, 24, 'PLANT')]
    }),
    ("Când trebuie să ud lalea", {
        "entities": [(19, 24, 'PLANT')]
    }),
    ("Când trebuie să ud laleei", {
        "entities": [(19, 25, 'PLANT')]
    }),
    ("Ce frecvență de udare are lalea", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 31, 'PLANT')]
    }),
    ("Ce frecvență de udare are lalea", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 31, 'PLANT')]
    }),
    ("Ce frecvență de udare are laleei", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 32, 'PLANT')]
    }),
    ("Cât de des ud lalea", {
        "entities": [(14, 19, 'PLANT')]
    }),
    ("Cât de des ud lalea", {
        "entities": [(14, 19, 'PLANT')]
    }),
    ("Cât de des ud laleei", {
        "entities": [(14, 20, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la lalea", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 29, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la lalea", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 29, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la laleei", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 30, 'PLANT')]
    }),
    ("Câtă lumină necesită lalea", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 26, 'PLANT')]
    }),
    ("Câtă lumină necesită lalea", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 26, 'PLANT')]
    }),
    ("Câtă lumină necesită laleei", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 27, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru lalea", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 42, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru lalea", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 42, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru laleei", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 43, 'PLANT')]
    }),
    ("lalea are nevoie de lumină", {
        "entities": [(0, 5, 'PLANT'), (20, 26, 'CARE_ASPECT')]
    }),
    ("lalea are nevoie de lumină", {
        "entities": [(0, 5, 'PLANT'), (20, 26, 'CARE_ASPECT')]
    }),
    ("laleei are nevoie de lumină", {
        "entities": [(0, 6, 'PLANT'), (21, 27, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru lalea", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 33, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru lalea", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 33, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru laleei", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 34, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru lalea", {
        "entities": [(34, 39, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru lalea", {
        "entities": [(34, 39, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru laleei", {
        "entities": [(34, 40, 'PLANT')]
    }),
    ("Când schimb substratul la lalea", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Când schimb substratul la lalea", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Când schimb substratul la laleei", {
        "entities": [(26, 32, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la lalea", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la lalea", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la laleei", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 35, 'PLANT')]
    }),
    ("lalea are lipsa inflorire", {
        "entities": [(0, 5, 'PLANT'), (10, 25, 'PROBLEM')]
    }),
    ("lalea are lipsa inflorire", {
        "entities": [(0, 5, 'PLANT'), (10, 25, 'PROBLEM')]
    }),
    ("laleei are lipsa inflorire", {
        "entities": [(0, 6, 'PLANT'), (11, 26, 'PROBLEM')]
    }),
    ("De ce are lalea lipsa inflorire", {
        "entities": [(10, 15, 'PLANT'), (16, 31, 'PROBLEM')]
    }),
    ("De ce are lalea lipsa inflorire", {
        "entities": [(10, 15, 'PLANT'), (16, 31, 'PROBLEM')]
    }),
    ("De ce are laleei lipsa inflorire", {
        "entities": [(10, 16, 'PLANT'), (17, 32, 'PROBLEM')]
    }),
    ("lipsa inflorire la lalea", {
        "entities": [(0, 15, 'PROBLEM'), (19, 24, 'PLANT')]
    }),
    ("lipsa inflorire la lalea", {
        "entities": [(0, 15, 'PROBLEM'), (19, 24, 'PLANT')]
    }),
    ("lipsa inflorire la laleei", {
        "entities": [(0, 15, 'PROBLEM'), (19, 25, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la lalea", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la lalea", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la laleei", {
        "entities": [(12, 27, 'PROBLEM'), (31, 37, 'PLANT')]
    }),
    ("lalea are tulpini scurte", {
        "entities": [(0, 5, 'PLANT'), (10, 24, 'PROBLEM')]
    }),
    ("lalea are tulpini scurte", {
        "entities": [(0, 5, 'PLANT'), (10, 24, 'PROBLEM')]
    }),
    ("laleei are tulpini scurte", {
        "entities": [(0, 6, 'PLANT'), (11, 25, 'PROBLEM')]
    }),
    ("De ce are lalea tulpini scurte", {
        "entities": [(10, 15, 'PLANT'), (16, 30, 'PROBLEM')]
    }),
    ("De ce are lalea tulpini scurte", {
        "entities": [(10, 15, 'PLANT'), (16, 30, 'PROBLEM')]
    }),
    ("De ce are laleei tulpini scurte", {
        "entities": [(10, 16, 'PLANT'), (17, 31, 'PROBLEM')]
    }),
    ("tulpini scurte la lalea", {
        "entities": [(0, 14, 'PROBLEM'), (18, 23, 'PLANT')]
    }),
    ("tulpini scurte la lalea", {
        "entities": [(0, 14, 'PROBLEM'), (18, 23, 'PLANT')]
    }),
    ("tulpini scurte la laleei", {
        "entities": [(0, 14, 'PROBLEM'), (18, 24, 'PLANT')]
    }),
    ("Probleme cu tulpini scurte la lalea", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Probleme cu tulpini scurte la lalea", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Probleme cu tulpini scurte la laleei", {
        "entities": [(12, 26, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("lalea are putrezirea bulbilor", {
        "entities": [(0, 5, 'PLANT'), (10, 29, 'PROBLEM')]
    }),
    ("lalea are putrezirea bulbilor", {
        "entities": [(0, 5, 'PLANT'), (10, 29, 'PROBLEM')]
    }),
    ("laleei are putrezirea bulbilor", {
        "entities": [(0, 6, 'PLANT'), (11, 30, 'PROBLEM')]
    }),
    ("De ce are lalea putrezirea bulbilor", {
        "entities": [(10, 15, 'PLANT'), (16, 35, 'PROBLEM')]
    }),
    ("De ce are lalea putrezirea bulbilor", {
        "entities": [(10, 15, 'PLANT'), (16, 35, 'PROBLEM')]
    }),
    ("De ce are laleei putrezirea bulbilor", {
        "entities": [(10, 16, 'PLANT'), (17, 36, 'PROBLEM')]
    }),
    ("putrezirea bulbilor la lalea", {
        "entities": [(0, 19, 'PROBLEM'), (23, 28, 'PLANT')]
    }),
    ("putrezirea bulbilor la lalea", {
        "entities": [(0, 19, 'PROBLEM'), (23, 28, 'PLANT')]
    }),
    ("putrezirea bulbilor la laleei", {
        "entities": [(0, 19, 'PROBLEM'), (23, 29, 'PLANT')]
    }),
    ("Probleme cu putrezirea bulbilor la lalea", {
        "entities": [(12, 31, 'PROBLEM'), (35, 40, 'PLANT')]
    }),
    ("Probleme cu putrezirea bulbilor la lalea", {
        "entities": [(12, 31, 'PROBLEM'), (35, 40, 'PLANT')]
    }),
    ("Probleme cu putrezirea bulbilor la laleei", {
        "entities": [(12, 31, 'PROBLEM'), (35, 41, 'PLANT')]
    }),
    ("Cum ud bujor", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Cum ud bujorul", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Cum ud bujorului", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Când trebuie să ud bujor", {
        "entities": [(19, 24, 'PLANT')]
    }),
    ("Când trebuie să ud bujorul", {
        "entities": [(19, 26, 'PLANT')]
    }),
    ("Când trebuie să ud bujorului", {
        "entities": [(19, 28, 'PLANT')]
    }),
    ("Ce frecvență de udare are bujor", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 31, 'PLANT')]
    }),
    ("Ce frecvență de udare are bujorul", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 33, 'PLANT')]
    }),
    ("Ce frecvență de udare are bujorului", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 35, 'PLANT')]
    }),
    ("Cât de des ud bujor", {
        "entities": [(14, 19, 'PLANT')]
    }),
    ("Cât de des ud bujorul", {
        "entities": [(14, 21, 'PLANT')]
    }),
    ("Cât de des ud bujorului", {
        "entities": [(14, 23, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la bujor", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 29, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la bujorul", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 31, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la bujorului", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 33, 'PLANT')]
    }),
    ("Câtă lumină necesită bujor", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 26, 'PLANT')]
    }),
    ("Câtă lumină necesită bujorul", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 28, 'PLANT')]
    }),
    ("Câtă lumină necesită bujorului", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 30, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru bujor", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 42, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru bujorul", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 44, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru bujorului", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 46, 'PLANT')]
    }),
    ("bujor are nevoie de lumină", {
        "entities": [(0, 5, 'PLANT'), (20, 26, 'CARE_ASPECT')]
    }),
    ("bujorul are nevoie de lumină", {
        "entities": [(0, 7, 'PLANT'), (22, 28, 'CARE_ASPECT')]
    }),
    ("bujorului are nevoie de lumină", {
        "entities": [(0, 9, 'PLANT'), (24, 30, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru bujor", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 33, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru bujorul", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 35, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru bujorului", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 37, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru bujor", {
        "entities": [(34, 39, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru bujorul", {
        "entities": [(34, 41, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru bujorului", {
        "entities": [(34, 43, 'PLANT')]
    }),
    ("Când schimb substratul la bujor", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Când schimb substratul la bujorul", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Când schimb substratul la bujorului", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la bujor", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 34, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la bujorul", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 36, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la bujorului", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 38, 'PLANT')]
    }),
    ("bujor are lipsa inflorire", {
        "entities": [(0, 5, 'PLANT'), (10, 25, 'PROBLEM')]
    }),
    ("bujorul are lipsa inflorire", {
        "entities": [(0, 7, 'PLANT'), (12, 27, 'PROBLEM')]
    }),
    ("bujorului are lipsa inflorire", {
        "entities": [(0, 9, 'PLANT'), (14, 29, 'PROBLEM')]
    }),
    ("De ce are bujor lipsa inflorire", {
        "entities": [(10, 15, 'PLANT'), (16, 31, 'PROBLEM')]
    }),
    ("De ce are bujorul lipsa inflorire", {
        "entities": [(10, 17, 'PLANT'), (18, 33, 'PROBLEM')]
    }),
    ("De ce are bujorului lipsa inflorire", {
        "entities": [(10, 19, 'PLANT'), (20, 35, 'PROBLEM')]
    }),
    ("lipsa inflorire la bujor", {
        "entities": [(0, 15, 'PROBLEM'), (19, 24, 'PLANT')]
    }),
    ("lipsa inflorire la bujorul", {
        "entities": [(0, 15, 'PROBLEM'), (19, 26, 'PLANT')]
    }),
    ("lipsa inflorire la bujorului", {
        "entities": [(0, 15, 'PROBLEM'), (19, 28, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la bujor", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la bujorul", {
        "entities": [(12, 27, 'PROBLEM'), (31, 38, 'PLANT')]
    }),
    ("Probleme cu lipsa inflorire la bujorului", {
        "entities": [(12, 27, 'PROBLEM'), (31, 40, 'PLANT')]
    }),
    ("bujor are frunze patate", {
        "entities": [(0, 5, 'PLANT'), (10, 23, 'PROBLEM')]
    }),
    ("bujorul are frunze patate", {
        "entities": [(0, 7, 'PLANT'), (12, 25, 'PROBLEM')]
    }),
    ("bujorului are frunze patate", {
        "entities": [(0, 9, 'PLANT'), (14, 27, 'PROBLEM')]
    }),
    ("De ce are bujor frunze patate", {
        "entities": [(10, 15, 'PLANT'), (16, 29, 'PROBLEM')]
    }),
    ("De ce are bujorul frunze patate", {
        "entities": [(10, 17, 'PLANT'), (18, 31, 'PROBLEM')]
    }),
    ("De ce are bujorului frunze patate", {
        "entities": [(10, 19, 'PLANT'), (20, 33, 'PROBLEM')]
    }),
    ("frunze patate la bujor", {
        "entities": [(0, 13, 'PROBLEM'), (17, 22, 'PLANT')]
    }),
    ("frunze patate la bujorul", {
        "entities": [(0, 13, 'PROBLEM'), (17, 24, 'PLANT')]
    }),
    ("frunze patate la bujorului", {
        "entities": [(0, 13, 'PROBLEM'), (17, 26, 'PLANT')]
    }),
    ("Probleme cu frunze patate la bujor", {
        "entities": [(12, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Probleme cu frunze patate la bujorul", {
        "entities": [(12, 25, 'PROBLEM'), (29, 36, 'PLANT')]
    }),
    ("Probleme cu frunze patate la bujorului", {
        "entities": [(12, 25, 'PROBLEM'), (29, 38, 'PLANT')]
    }),
    ("bujor are boboci care nu se deschid", {
        "entities": [(0, 5, 'PLANT'), (10, 35, 'PROBLEM')]
    }),
    ("bujorul are boboci care nu se deschid", {
        "entities": [(0, 7, 'PLANT'), (12, 37, 'PROBLEM')]
    }),
    ("bujorului are boboci care nu se deschid", {
        "entities": [(0, 9, 'PLANT'), (14, 39, 'PROBLEM')]
    }),
    ("De ce are bujor boboci care nu se deschid", {
        "entities": [(10, 15, 'PLANT'), (16, 41, 'PROBLEM')]
    }),
    ("De ce are bujorul boboci care nu se deschid", {
        "entities": [(10, 17, 'PLANT'), (18, 43, 'PROBLEM')]
    }),
    ("De ce are bujorului boboci care nu se deschid", {
        "entities": [(10, 19, 'PLANT'), (20, 45, 'PROBLEM')]
    }),
    ("boboci care nu se deschid la bujor", {
        "entities": [(0, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("boboci care nu se deschid la bujorul", {
        "entities": [(0, 25, 'PROBLEM'), (29, 36, 'PLANT')]
    }),
    ("boboci care nu se deschid la bujorului", {
        "entities": [(0, 25, 'PROBLEM'), (29, 38, 'PLANT')]
    }),
    ("Probleme cu boboci care nu se deschid la bujor", {
        "entities": [(12, 37, 'PROBLEM'), (41, 46, 'PLANT')]
    }),
    ("Probleme cu boboci care nu se deschid la bujorul", {
        "entities": [(12, 37, 'PROBLEM'), (41, 48, 'PLANT')]
    }),
    ("Probleme cu boboci care nu se deschid la bujorului", {
        "entities": [(12, 37, 'PROBLEM'), (41, 50, 'PLANT')]
    }),
    ("Cum ud magnolie", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Cum ud magnolia", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Cum ud magnoliei", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Când trebuie să ud magnolie", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Când trebuie să ud magnolia", {
        "entities": [(19, 27, 'PLANT')]
    }),
    ("Când trebuie să ud magnoliei", {
        "entities": [(19, 28, 'PLANT')]
    }),
    ("Ce frecvență de udare are magnolie", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Ce frecvență de udare are magnolia", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 34, 'PLANT')]
    }),
    ("Ce frecvență de udare are magnoliei", {
        "entities": [(16, 21, 'CARE_ASPECT'), (26, 35, 'PLANT')]
    }),
    ("Cât de des ud magnolie", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Cât de des ud magnolia", {
        "entities": [(14, 22, 'PLANT')]
    }),
    ("Cât de des ud magnoliei", {
        "entities": [(14, 23, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la magnolie", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la magnolia", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 32, 'PLANT')]
    }),
    ("Ce lumină îi trebuie la magnoliei", {
        "entities": [(3, 9, 'CARE_ASPECT'), (24, 33, 'PLANT')]
    }),
    ("Câtă lumină necesită magnolie", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Câtă lumină necesită magnolia", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 29, 'PLANT')]
    }),
    ("Câtă lumină necesită magnoliei", {
        "entities": [(5, 11, 'CARE_ASPECT'), (21, 30, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru magnolie", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru magnolia", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 45, 'PLANT')]
    }),
    ("Care sunt cerințele de lumină pentru magnoliei", {
        "entities": [(23, 29, 'CARE_ASPECT'), (37, 46, 'PLANT')]
    }),
    ("magnolie are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("magnolia are nevoie de lumină", {
        "entities": [(0, 8, 'PLANT'), (23, 29, 'CARE_ASPECT')]
    }),
    ("magnoliei are nevoie de lumină", {
        "entities": [(0, 9, 'PLANT'), (24, 30, 'CARE_ASPECT')]
    }),
    ("Ce substrat folosesc pentru magnolie", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru magnolia", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 36, 'PLANT')]
    }),
    ("Ce substrat folosesc pentru magnoliei", {
        "entities": [(3, 11, 'CARE_ASPECT'), (28, 37, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru magnolie", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru magnolia", {
        "entities": [(34, 42, 'PLANT')]
    }),
    ("Care e substratul potrivit pentru magnoliei", {
        "entities": [(34, 43, 'PLANT')]
    }),
    ("Când schimb substratul la magnolie", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Când schimb substratul la magnolia", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Când schimb substratul la magnoliei", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la magnolie", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la magnolia", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 37, 'PLANT')]
    }),
    ("Ce tip de pământ folosesc la magnoliei", {
        "entities": [(10, 16, 'CARE_ASPECT'), (29, 38, 'PLANT')]
    }),
    ("magnolie are inghet flori", {
        "entities": [(0, 8, 'PLANT'), (13, 25, 'PROBLEM')]
    }),
    ("magnolia are inghet flori", {
        "entities": [(0, 8, 'PLANT'), (13, 25, 'PROBLEM')]
    }),
    ("magnoliei are inghet flori", {
        "entities": [(0, 9, 'PLANT'), (14, 26, 'PROBLEM')]
    }),
    ("De ce are magnolie inghet flori", {
        "entities": [(10, 18, 'PLANT'), (19, 31, 'PROBLEM')]
    }),
    ("De ce are magnolia inghet flori", {
        "entities": [(10, 18, 'PLANT'), (19, 31, 'PROBLEM')]
    }),
    ("De ce are magnoliei inghet flori", {
        "entities": [(10, 19, 'PLANT'), (20, 32, 'PROBLEM')]
    }),
    ("inghet flori la magnolie", {
        "entities": [(0, 12, 'PROBLEM'), (16, 24, 'PLANT')]
    }),
    ("inghet flori la magnolia", {
        "entities": [(0, 12, 'PROBLEM'), (16, 24, 'PLANT')]
    }),
    ("inghet flori la magnoliei", {
        "entities": [(0, 12, 'PROBLEM'), (16, 25, 'PLANT')]
    }),
    ("Probleme cu inghet flori la magnolie", {
        "entities": [(12, 24, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("Probleme cu inghet flori la magnolia", {
        "entities": [(12, 24, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("Probleme cu inghet flori la magnoliei", {
        "entities": [(12, 24, 'PROBLEM'), (28, 37, 'PLANT')]
    }),
    ("magnolie are frunze galbene", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("magnolia are frunze galbene", {
        "entities": [(0, 8, 'PLANT'), (13, 27, 'PROBLEM')]
    }),
    ("magnoliei are frunze galbene", {
        "entities": [(0, 9, 'PLANT'), (14, 28, 'PROBLEM')]
    }),
    ("De ce are magnolie frunze galbene", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("De ce are magnolia frunze galbene", {
        "entities": [(10, 18, 'PLANT'), (19, 33, 'PROBLEM')]
    }),
    ("De ce are magnoliei frunze galbene", {
        "entities": [(10, 19, 'PLANT'), (20, 34, 'PROBLEM')]
    }),
    ("frunze galbene la magnolie", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("frunze galbene la magnolia", {
        "entities": [(0, 14, 'PROBLEM'), (18, 26, 'PLANT')]
    }),
    ("frunze galbene la magnoliei", {
        "entities": [(0, 14, 'PROBLEM'), (18, 27, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la magnolie", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la magnolia", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("Probleme cu frunze galbene la magnoliei", {
        "entities": [(12, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("magnolie are scoarta deteriorata", {
        "entities": [(0, 8, 'PLANT'), (13, 32, 'PROBLEM')]
    }),
    ("magnolia are scoarta deteriorata", {
        "entities": [(0, 8, 'PLANT'), (13, 32, 'PROBLEM')]
    }),
    ("magnoliei are scoarta deteriorata", {
        "entities": [(0, 9, 'PLANT'), (14, 33, 'PROBLEM')]
    }),
    ("De ce are magnolie scoarta deteriorata", {
        "entities": [(10, 18, 'PLANT'), (19, 38, 'PROBLEM')]
    }),
    ("De ce are magnolia scoarta deteriorata", {
        "entities": [(10, 18, 'PLANT'), (19, 38, 'PROBLEM')]
    }),
    ("De ce are magnoliei scoarta deteriorata", {
        "entities": [(10, 19, 'PLANT'), (20, 39, 'PROBLEM')]
    }),
    ("scoarta deteriorata la magnolie", {
        "entities": [(0, 19, 'PROBLEM'), (23, 31, 'PLANT')]
    }),
    ("scoarta deteriorata la magnolia", {
        "entities": [(0, 19, 'PROBLEM'), (23, 31, 'PLANT')]
    }),
    ("scoarta deteriorata la magnoliei", {
        "entities": [(0, 19, 'PROBLEM'), (23, 32, 'PLANT')]
    }),
    ("Probleme cu scoarta deteriorata la magnolie", {
        "entities": [(12, 31, 'PROBLEM'), (35, 43, 'PLANT')]
    }),
    ("Probleme cu scoarta deteriorata la magnolia", {
        "entities": [(12, 31, 'PROBLEM'), (35, 43, 'PLANT')]
    }),
    ("Probleme cu scoarta deteriorata la magnoliei", {
        "entities": [(12, 31, 'PROBLEM'), (35, 44, 'PLANT')]
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

# Lista de entități cunoscute pentru referință
ENTITIES = {
    "PLANT": ['orhidee', 'orhidea', 'orhideei', 'ficus', 'ficusul', 'ficusului', 'trandafir', 'trandafirul', 'trandafirului', 'crin', 'crinul', 'crinului', 'muscata', 'muscata', 'muscatei', 'aloe vera', 'aloe vera', 'aloe verei', 'cactus', 'cactusul', 'cactusului', 'lavanda', 'lavanda', 'lavandei', 'lalea', 'lalea', 'laleei', 'bujor', 'bujorul', 'bujorului', 'magnolie', 'magnolia', 'magnoliei'],
    "CARE_ASPECT": ['udare', 'lumina', 'substrat', 'lumină', 'pământ', 'sol'],
    "PROBLEM": ['frunze galbene', 'radacini putrede', 'cadere frunze', 'frunze galbene', 'frunze galbene', 'pete negre', 'ingalbenirea frunzelor', 'lipsa inflorire', 'frunze galbene', 'putine flori', 'frunze maro', 'frunze moi', 'putrezirea bazei', 'putrezire baza', 'crestere alungita', 'pete maronii', 'putrezire radacini', 'crestere lemnoasa', 'frunze galbene', 'lipsa inflorire', 'tulpini scurte', 'putrezirea bulbilor', 'lipsa inflorire', 'frunze patate', 'boboci care nu se deschid', 'inghet flori', 'frunze galbene', 'scoarta deteriorata']
}