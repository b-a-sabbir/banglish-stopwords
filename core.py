import re
import string
from typing import List, Set

class BanglishStopwords:
    """
    A production-ready library to filter Banglish stopwords from text.
    Includes support for repeated characters (e.g., 'naaaa' -> 'na') and punctuation.
    """
    
    def __init__(self):
        # Flattened stopword set for O(1) lookup performance
        self._stopwords: Set[str] = {
            "atoeb", "otoeb", "otoeeb", "otob", "atob", "otoab", "otoyeb", "othoco", "othochcho", 
            "othoch", "otoc", "ochoco", "othsho", "othsh", "othocho", "othoba", "athoba", 
            "othba", "otba", "athba", "othb", "onujayi", "onuyayi", "onujai", "onuyai", 
            "onujayee", "onujaiyi", "onk", "onek", "anek", "onke", "oneeeek", "anke", 
            "onkk", "oneq", "aneq", "oneke", "aneke", "oneqy", "oneky", "onekei", 
            "anekei", "onekey", "onkey", "ontoto", "antato", "ontotoo", "ontto", 
            "ontot", "antat", "onno", "anno", "onnoo", "onn", "ann", "obodi", 
            "abodhi", "abodi", "obdi", "abdi", "obosso", "oboshso", "oboshshoi", 
            "obossoi", "obossyoi", "obshsho", "orthoat", "ortat", "orthat", "orthot", 
            "othat", "ortt", "ortht", "ai", "i", "ay", "agami", "agamee", "agm", 
            "age", "aage", "agee", "agay", "ag", "agey", "agei", "aagei", "ageye", 
            "agai", "ache", "achhe", "achee", "achhei", "ase", "achey", "ashey", 
            "asey", "asei", "aj", "aaj", "ajke", "az", "azke", "adyovage", "adyobhage", 
            "addovage", "apnar", "apnr", "apner", "apni", "apnee", "apn", "apney", 
            "abar", "abr", "abaroo", "abrr", "amra", "amraa", "amrra", "amr", "amake", 
            "amk", "amke", "amq", "amakei", "amader", "amdr", "amadr", "amader", 
            "amar", "amrr", "amarr", "ami", "amii", "amee", "mi", "amy", "amei", 
            "ar", "aar", "r", "arr", "aro", "aroo", "aaro", "r-o", "aroh", "ii", 
            "ee", "y", "itiadi", "ityadi", "ityadii", "etadi", "ittadi", "iha", 
            "ihaa", "eha", "uchit", "ucit", "ucht", "uttor", "utor", "uttr", "uni", 
            "unee", "uny", "upor", "upore", "upr", "upre", "uprey", "e", "ee", 
            "ender", "endr", "endher", "enra", "enraa", "ei", "eii", "ey", "ekoi", 
            "ekai", "eki", "eky", "ekti", "ekta", "ektee", "kti", "akta", "ekbar", 
            "ekbaar", "akbar", "eke", "ake", "ekhon", "akhon", "ekhn", "akhn", "ekn", 
            "ekhono", "akhono", "ekhno", "eta", "et", "ata", "ataa", "etai", "atai", 
            "etay", "eti", "etii", "etee", "ety", "eto", "ato", "etoo", "etotai", 
            "atotai", "ete", "ate", "eder", "edr", "adr", "ebong", "ebon", "abong", 
            "ebng", "abng", "ebar", "abar", "abr", "emon", "amon", "emn", "amn", 
            "emonki", "ammonki", "emnki", "emni", "amni", "emny", "er", "err", "era", 
            "ara", "el", "elo", "alo", "esho", "eso", "asho", "eshe", "ese", "ase", 
            "asay", "oi", "oy", "o", "oo", "onder", "onoder", "ondr", "onr", "onor", 
            "onra", "onraa", "oke", "ok", "okey", "okhane", "okhne", "oder", "odr", 
            "odher", "or", "orr", "orh", "ora", "oraa", "orah", "kokhono", "kokhonoo", 
            "kokhon-o", "kokhno", "koto", "kotoo", "kto", "kt", "kobe", "kbe", "kb", 
            "kemne", "kemone", "komne", "koyek", "koiek", "koiaq", "koyekti", "koiekti", 
            "korche", "korse", "krche", "krse", "korsey", "korchen", "korsen", "krcen", 
            "korte", "krte", "krt", "korbe", "krbe", "krb", "korben", "krben", "krbn", 
            "korle", "krle", "krl", "korlen", "krlen", "krln", "kora", "kra", "kraa", 
            "korai", "krai", "koray", "kray", "korar", "krar", "krr", "kori", "kri", 
            "kry", "korite", "krite", "koriya", "koria", "kria", "koriye", "korie", 
            "krie", "kore", "kre", "kr", "krey", "korei", "krei", "korechilen", 
            "korsilen", "krsilen", "koreche", "korse", "krse", "korechen", "korsen", 
            "krsen", "koren", "kren", "krn", "kauke", "kawke", "kauk", "kaoqe", "kach", 
            "kachh", "kache", "kachhe", "kase", "kashe", "kasey", "kaj", "kaaj", "kj", 
            "kaz", "kaje", "kaaje", "kje", "kaze", "karo", "karoo", "karor", "kro", 
            "karron", "karon", "karn", "krn", "ki", "kii", "q", "ky", "kee", "kimba", 
            "kingba", "kichu", "kishu", "kisu", "kichoo", "kichui", "kisui", "kintu", 
            "kntu", "kinto", "ke", "k", "keu", "kew", "keo", "keui", "kewi", "dekha", 
            "dkha", "keno", "kano", "kn", "kno", "qeno", "koti", "kuty", "kon", "kun", 
            "kono", "kno", "kuno", "khetre", "khettre", "khub", "khoob", "khb", "giye", 
            "gie", "gy", "gye", "giyeche", "gese", "gyese", "guli", "gulo", "glo", 
            "geche", "gache", "gese", "gelo", "gel", "gl", "gele", "gle", "gota", 
            "guta", "chole", "chan", "chaan", "can", "chay", "chai", "cai", "char", 
            "car", "4", "chalu", "calu", "cheye", "ceye", "caia", "chesta", "cesta", 
            "chara", "sara", "shara", "charao", "sarao", "chilo", "silo", "sil", 
            "chilen", "silen", "jon", "jn", "jun", "jonke", "jnke", "joner", "jner", 
            "jonno", "jnno", "jono", "jonne", "jante", "jnte", "jana", "jna", "janano", 
            "jnano", "janay", "janai", "janiye", "janie", "janiyeche", "janiese", 
            "je", "j", "z", "ti", "tee", "ty", "t", "thik", "theek", "thk", "tokhon", 
            "tokhn", "tkhn", "toto", "tto", "totha", "tobu", "tobuo", "tbuo", "tobe", 
            "tbe", "tb", "ta", "taa", "th", "take", "tanke", "tke", "tander", "tanr", 
            "tr", "tanra", "tra", "tai", "tay", "ty", "tao", "to", "tkey", "tate", 
            "tte", "tader", "tadr", "tadher", "thar", "tarpor", "trpor", "tara", 
            "tahole", "tahle", "thle", "tini", "tny", "tinio", "tumi", "tmi", "tm", 
            "tumee", "tule", "tle", "temon", "temn", "toh", "tomar", "tomr", "tmr", 
            "thkbe", "thkb", "thake", "thk", "thke", "thaken", "thken", "theke", 
            "thke", "thk", "thekei", "dke", "dte", "din", "dn", "diye", "die", "dye", 
            "dy", "diyeche", "dyese", "diyechen", "dyesen", "dilen", "dlen", "du", 
            "2", "dui", "duy", "duti", "2ta", "duto", "2to", "dewa", "deoa", "dowa", 
            "dea", "dewar", "deoar", "dawar", "dekhte", "dkhte", "dekhe", "dke", 
            "den", "dey", "dei", "dbara", "dara", "dhora", "dhra", "dhore", "dhre", 
            "notun", "nutun", "ntn", "noy", "noi", "ny", "na", "naa", "n", "nah", 
            "nh", "nai", "nay", "naki", "nky", "nagad", "ngad", "nana", "nije", "nj", 
            "nijei", "nijeder", "nijedr", "nijer", "njr", "nite", "nte", "niye", 
            "nie", "nye", "nei", "ney", "ni", "newa", "neoa", "nowa", "pokkho", 
            "pkho", "por", "pr", "pore", "pre", "prey", "poreo", "porjonto", "prjnto", 
            "pawa", "paoa", "powa", "pach", "5", "pari", "pri", "pare", "pre", "pry", 
            "paren", "pren", "peye", "peie", "pye", "proti", "prti", "prothom", 
            "prthom", "1st", "prothomik", "prathomik", "pray", "prai", "pry", "fole", 
            "phole", "fle", "fire", "phire", "fre", "fer", "pher", "fr", "boktobbo", 
            "boktob", "bodle", "bdle", "bon", "bn", "borong", "brng", "bolte", "blte", 
            "bollo", "bll", "bollen", "bllen", "bola", "bla", "bole", "ble", "bl", 
            "bolechen", "blsen", "bolen", "blen", "bose", "bse", "bohu", "ba", "baa", 
            "bah", "bade", "bde", "bar", "br", "barr", "bi", "b", "bina", "bibhinno", 
            "bivinno", "bishesh", "bises", "bisoyti", "bishoyti", "besh", "bes", 
            "beshi", "besi", "bsi", "bebohar", "babohar", "bapare", "bappare", "bhabe", 
            "vabe", "vbe", "bhabei", "vabei", "moto", "mto", "mt", "moddhovage", 
            "moddhobhage", "moddhe", "modhe", "mdhe", "moddey", "mone", "mne", 
            "matro", "mtro", "madhyome", "maddhome", "madhome", "mot", "mt", "jokhon", 
            "jokhn", "jkhn", "joto", "jto", "jotota", "jotheshto", "jotesto", "jodi", 
            "jdi", "jody", "jodio", "jdio", "ja", "j", "jaa", "jawa", "jaoa", "jowa", 
            "jaowa", "jawar", "jaoar", "jake", "jke", "jacche", "jasse", "jace", 
            "jate", "jte", "jader", "jadr", "jan", "jn", "jabe", "jbe", "jay", "jai", 
            "jy", "jar", "jr", "jara", "jra", "jini", "jni", "je", "z", "jekhane", 
            "jekhne", "jkhne", "jete", "jte", "jeno", "jno", "jemon", "jemn", "ro", 
            "rokom", "rkm", "royeche", "royese", "rese", "rakha", "rkha", "rekhe", 
            "rkhe", "shudhu", "sudhu", "shudu", "shd", "shuru", "suru", "shru", "songe", 
            "shonge", "sange", "snge", "sob", "shob", "sb", "sobar", "sbar", "somosto", 
            "shomosto", "smsto", "somproti", "smproti", "soho", "shoho", "sho", 
            "sohit", "sadharon", "shadharon", "sdron", "samne", "shamne", "smne", 
            "si", "s", "sutorang", "shutorang", "sutrng", "se", "she", "s", "sei", 
            "shei", "sey", "sekhan", "skhn", "sekhane", "shekhane", "skhne", "seta", 
            "sheta", "sta", "setai", "stai", "setao", "stao", "seti", "sty", "sposhto", 
            "sposto", "shoyong", "soyong", "hoite", "hte", "hoibe", "hoibey", "hoiya", 
            "hoia", "howa", "haoa", "hoa", "howay", "haoay", "howar", "haoar", 
            "hocche", "hoche", "hcce", "hsse", "hoto", "hto", "hote", "hte", "hotei", 
            "hon", "hn", "hobe", "hbe", "hb", "hobey", "hoben", "hben", "hoy", "hoi", 
            "hy", "hoyto", "hoito", "hyto", "hoyni", "hoini", "hye", "hoie", "hoe", 
            "hye", "hoyechilo", "hoyesilo", "hysilo", "hoyeche", "hoyese", "hyese", 
            "hoyechen", "hoyesen", "holo", "hol", "hl", "hole", "hle", "holei", 
            "hlei", "holeo", "hleo", "hlow", "hjr", "1000", "hajar", "hajr", "hisabe", 
            "hishebe", "hsbe", "hoile", "hle", "hok", "hk", "hoq"
        }
        self._repeat_regex = re.compile(r'(.)\1+')

    def _reduce_repetitions(self, word: str) -> str:
        """Reduces repeated characters like 'naaaa' to 'na'."""
        return self._repeat_regex.sub(r'\1', word)

    def is_stopword(self, word: str) -> bool:
        """Returns True if the word is a Banglish stopword."""
        if not word: return False
        
        clean_w = word.lower().strip(string.punctuation)
        if clean_w in self._stopwords:
            return True
        
        # Check by reducing repeated characters (onekkk -> onek)
        if self._reduce_repetitions(clean_w) in self._stopwords:
            return True
        return False

    def remove_stopwords(self, text: str) -> str:
        """Filters out stopwords from a given text string."""
        if not text: return ""
        
        # Split by whitespace but keep punctuation attached to words initially
        words = text.split()
        filtered = [w for w in words if not self.is_stopword(w)]
        
        return " ".join(filtered)

    def get_stopwords(self) -> Set[str]:
        """Returns the complete set of supported Banglish stopwords."""
        return self._stopwords

# --- Example Usage ---
if __name__ == "__main__":
    bn_nlp = BanglishStopwords()
    input_text = "Ami r tmi ekhon bhalo achhiiiii, kintu hbeee naaa! apni abar ashen."
    
    clean_text = bn_nlp.remove_stopwords(input_text)
    print(f"Cleaned Text: {clean_text}")