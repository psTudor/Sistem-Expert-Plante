PLANT_NOT_SPECIFIED = (
    "Îmi pare rău, dar nu am înțeles despre ce plantă vorbești. "
    "Poți să specifici numele plantei?"
)
PLANT_NOT_FOUND = (
    "Îmi pare rău, dar nu am informații despre planta '{plant}' în baza mea de cunoștințe."
)
NEEDS_REPHRASE = (
    "Am înțeles că te interesează {plant}, dar nu sunt sigur ce anume vrei să știi despre această plantă. "
    "Poți să reformulezi întrebarea?"
)
GENERIC_ERROR = "A apărut o eroare neașteptată: {error}"
FIREBASE_ERROR = "Eroare la incarcarea datelor din Firebase: {error}"
EXPERT_ERROR = "A apărut o eroare la apelarea expert system: {error}"
KNOWLEDGEBASE_ERROR = "Eroare la accesarea bazei de cunoștințe: {error}"
FILE_NOT_FOUND_MSG = "Nu s-a găsit fișierul: {path}"
ALTERNATIVE_FILE = "Nu s-a găsit fișierul de date: {data_file} sau {alternative_path}"
PLANT_DATA_LOAD_ERROR = "Nu s-au putut încărca datele despre plante."
NO_IDENTIFICATION_RESULTS = "Nu s-au găsit rezultate de identificare."
API_ERROR_STATUS = "Eroare API: cod de răspuns {status_code}"
API_ERROR_BODY = "Răspuns API: {response_text}"
IMAGE_FILE_NOT_FOUND = "Fișierul imagine nu a fost găsit."
PLANT_IDENTIFICATION_ERROR = "Eroare la identificarea plantei."
JSON_DECODE_ERROR = "Eroare la parsarea JSON: {error}"
JSON_FILE_NOT_FOUND = "Fișierul JSON {path} nu a fost găsit."
PLANTS_DATA_MISSING = "Nu s-au găsit date despre plante în fișierul JSON."
PLANTS_DATA_LOADED = "S-au încărcat {count} plante din fișierul JSON."
INVALID_JSON_STRUCTURE = "Format incorect al fișierului de date: lipsește cheia 'plants'."
API_ERROR_PLANTS_LIST = "Eroare la obținerea listei de plante: {error}"
API_ERROR_PLANT_INFO = "Eroare la obținerea informațiilor despre plantă: {error}"
API_ERROR_QUERY = "Eroare la trimiterea interogării: {error}"
API_ERROR_UPLOAD = "Eroare la încărcarea imaginii: {error}"
API_GENERIC_RESPONSE_FAIL = "Îmi pare rău, a apărut o eroare în procesarea cererii tale."
MIGRATION_SUMMARY = "Migrare completă: {success}/{total} plante au fost migrate cu succes."
