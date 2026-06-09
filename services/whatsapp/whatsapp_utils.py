import logging
from datetime import datetime
from services.config import load_config
from services.whatsapp_sender import send_paste_report

CONFIG = load_config()


# SEND ADMIN NOTIFICATION WITH TIMESTAMP
def admin_authentication(message: str, is_critical: bool = False):
    try:
        admin_number = CONFIG["ADMIN_PRIMARY"]
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        admin_notification = f"[{timestamp}] {message}"
        send_paste_report(admin_number, admin_notification)
        logging.info("[SYSTEM] ADMIN NOTIFICATION SUCCESSFULLY SENT")
    except Exception as e:
        logging.error(f"[ERROR] ADMIN NOTIFICATION FAILED: {str(e)}")


# LIST OF ALL ACTIVE BRANCH IDS
def get_branch_scope() -> list[str]:
    return [
        "1501",  # KEDOYA (JABODETABEKSER)
        "1502",  # SUNTER (JABODETABEKSER)
        "1503",  # DENPASAR (IBT)
        "1504",  # SURABAYA (JAWA TIMUR)
        "1505",  # BANDUNG (JAWA BARAT)
        "1506",  # BEKASI (JABODETABEKSER)
        "1507",  # TANGERANG (JABODETABEKSER)
        "1508",  # KARAWANG (JAWA BARAT)
        "1509",  # YOGYAKARTA (JAWA TENGAH)
        "1510",  # SEMARANG (JAWA TENGAH)
        "1511",  # SAMARINDA (KALIMANTAN)
        "1512",  # BOGOR (JABODETABEKSER)
        "1513",  # MALANG (JAWA TIMUR)
        "1514",  # MAKASSAR (SULAWESI)
        "1515",  # KUDUS (JAWA TENGAH)
        "1516",  # SERANG (JABODETABEKSER)
        "1517",  # PURWOKERTO (JAWA TENGAH)
        "1518",  # DEWI SARTIKA (JABODETABEKSER)
        "1519",  # GRESIK (JAWA TIMUR)
        "1520",  # PEKANBARU (SUMBAGUTENG)
        "1521",  # BANJARMASIN (KALIMANTAN)
        "1522",  # MEDAN (SUMBAGUTENG)
        "1523",  # BATAM (SUMBAGUTENG)
        "1524",  # TEGAL (JAWA TENGAH)
        "1525",  # KEDIRI (JAWA TIMUR)
        "1526",  # MATARAM (IBT)
        "1527",  # PADANG (SUMBAGUTENG)
        "1528",  # CIREBON (JAWA BARAT)
        "1529",  # BALIKPAPAN (KALIMANTAN)
        "1531",  # KUPANG (IBT)
        "1532",  # BENGKULU (SUMBAGSEL)
        "1533",  # MANADO (SULAWESI)
        "1534",  # SOLO (JAWA TENGAH)
        "1535",  # PALEMBANG (SUMBAGSEL)
        "1536",  # BANDAR LAMPUNG (SUMBAGSEL)
        "1537",  # PALANGKARAYA (KALIMANTAN)
        "1538",  # PANGKAL PINANG (SUMBAGSEL)
        "1539",  # GORONTALO (SULAWESI)
        "1540",  # PALU (SULAWESI)
        "1541",  # KENDARI (SULAWESI)
        "1542",  # JAMBI (SUMBAGSEL)
        "1543",  # DEPOK (JABODETABEKSER)
        "1545",  # MEDAN (SUMBAGUTENG)
        "1546",  # BANDAR LAMPUNG (SUMBAGSEL)
        "1547",  # TERNATE (SULAWESI)
        "1549",  # SURABAYA (JAWA TIMUR)
        "1550",  # BARABAI (KALIMANTAN)
        "1551",  # PARE PARE (SULAWESI)
        "1552",  # SAMPIT (KALIMANTAN)
        "1553",  # PONTIANAK (KALIMANTAN)
        "1554",  # TASIKMALAYA (JAWA BARAT)
    ]


# LIST OF AREAS (GROUPING BRANCHES)
def get_area_scope() -> list[str]:
    return [
        "JABODETABEKSER",  # 8 BRANCHES -> 1501, 1502, 1506, 1507, 1512, 1516, 1518, 1543
        "JAWA BARAT",  # 4 BRANCHES -> 1505, 1508, 1528, 1554
        "JAWA TENGAH",  # 6 BRANCHES -> 1509, 1510, 1515, 1517, 1524, 1534
        "JAWA TIMUR",  # 5 BRANCHES -> 1504, 1513, 1519, 1525, 1549
        "KALIMANTAN",  # 7 BRANCHES -> 1511, 1521, 1529, 1537, 1550, 1552, 1553
        "SULAWESI",  # 7 BRANCHES -> 1514, 1533, 1539, 1540, 1541, 1547, 1551
        "SUMBAGSEL",  # 6 BRANCHES -> 1532, 1535, 1536, 1538, 1542, 1546
        "SUMBAGUTENG",  # 5 BRANCHES -> 1520, 1522, 1523, 1527, 1545
        "IBT",  # 3 BRANCHES -> 1503, 1526, 1531
    ]
