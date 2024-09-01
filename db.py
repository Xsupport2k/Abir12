import utility as utl


cs = utl.Database()
cs = cs.data()

def alter_table(cs, sql):
    try:
        cs.execute(sql)
    except:
        pass
    try:
        sql_split = sql.split(" ")
        if sql[0:11] == 'ALTER TABLE':
            if 'UNIQUE' in sql:
                try:
                    cs.execute(f"ALTER TABLE {sql_split[2]} ADD CONSTRAINT {sql_split[4]} UNIQUE({sql_split[4]})")
                except:
                    pass
            sql = sql.replace("ADD", "CHANGE").replace(" UNIQUE", "")
            sql = sql.split(' AFTER')[0].replace(f" {sql_split[4]} ", f" {sql_split[4]} {sql_split[4]} ") + " AFTER" + sql.split(' AFTER')[1]
            cs.execute(sql)
    except:
        pass


alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.admin} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD channel_1 VARCHAR(50) DEFAULT NULL AFTER id")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD channel_2 VARCHAR(50) DEFAULT NULL AFTER channel_1")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD channel_3 VARCHAR(50) DEFAULT NULL AFTER channel_2")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD support VARCHAR(50) DEFAULT NULL AFTER channel_3")
alter_table(cs, f" ALTER TABLE {ut(126, '🇯🇲', 'jm', 'Jamaica', 'jamaica', 1876, 5000, 1, 1),
(129, '🇯🇴', 'jo', 'Jordan', 'jordan', 962, 5000, 1, 1),
(130, '🇴🇲', 'om', 'Oman', 'oman', 968, 5000, 1, 1),
(131, '🇧🇭', 'bh', 'Bahrain', 'bahrain', 973, 5000, 1, 1),
(132, '🇶🇦', 'qa', 'Qatar', 'qatar', 974, 5000, 1, 1),
(133, '🇲🇳', 'mn', 'Mongolia', 'mongolia', 976, 5000, 1, 1),
(134, '🇲🇻', 'mv', 'Maldives', 'maldives', 960, 5000, 1, 1),
(135, '🇱🇾', 'ly', 'Libya', 'libya', 218, 5000, 1, 1),
(137, '🇧🇫', 'bf', 'Burkina Faso', 'burkina faso', 226, 5000, 1, 1),
(139, '🇧🇯', 'bj', 'Benin', 'benin', 229, 5000, 1, 1),
(141, '🇸🇴', 'so', 'Somalia', 'somalia', 252, 5000, 0, 1),
(142, '🇿🇼', 'zw', 'Zimbabwe', 'zimbabwe', 263, 5000, 1, 1),
(148, '🇨🇭', 'ch', 'Switzerland', 'switzerland', 41, 5000, 0, 1),
(150, '🇧🇧', 'bb', 'Barbados', 'barbados', 1246, 5000, 0, 1),
(155, '🇸🇬', 'sg', 'Singapore', 'singapore', 65, 5000, 1, 1),
(156, '🇹🇯', 'tj', 'Tajikistan', 'tajikistan', 992, 5000, 0, 1),
(159, '🇨🇾', 'cy', 'Cyprus', 'cyprus', 357, 5000, 0, 1);""")l.admin} ADD min_withdrawal INT(11) NOT NULL DEFAULT 10000 AFTER support" )
alter_table(cs, f"ALTER TABLE {utl.admin} ADD onoff_bot TINYINT(1) NOT NULL DEFAULT 1 AFTER min_withdrawal")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD onoff_account TINYINT(1) NOT NULL DEFAULT 1 AFTER onoff_bot")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD onoff_withdrawal TINYINT(1) NOT NULL DEFAULT 1 AFTER onoff_account")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD onoff_support TINYINT(1) NOT NULL DEFAULT 1 AFTER onoff_withdrawal")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD change_pass TINYINT(1) NOT NULL DEFAULT 0 AFTER onoff_support")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD is_change_profile TINYINT(1) NOT NULL DEFAULT 0 AFTER change_pass")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD is_set_username TINYINT(1) NOT NULL DEFAULT 0 AFTER is_change_profile")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD api_per_number INT(11) NOT NULL DEFAULT 5 AFTER is_set_username")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD time_logout_account INT(11) NOT NULL DEFAULT 900 AFTER api_per_number")
alter_table(cs, f"ALTER TABLE {utl.admin} ADD account_password varchar(64) DEFAULT NULL AFTER time_logout_account")


alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.apis} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.apis} ADD api_id INT(11) NOT NULL DEFAULT 0 AFTER id")
alter_table(cs, f"ALTER TABLE {utl.apis} ADD api_hash VARCHAR(50) DEFAULT NULL AFTER api_id")


alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.mbots} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD cat_id int(11) NOT NULL DEFAULT 0 AFTER id")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD creator_user_id BIGINT(20) DEFAULT NULL AFTER cat_id")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD phone VARCHAR(20) DEFAULT NULL AFTER creator_user_id")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD user_id BIGINT(20) DEFAULT NULL AFTER phone")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD status TINYINT(1) NOT NULL DEFAULT 0 AFTER user_id")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD country_id INT(11) NOT NULL DEFAULT 0 AFTER status")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD amount INT(11) NOT NULL DEFAULT 0 AFTER country_id")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD end_restrict INT(11) NOT NULL DEFAULT 0 AFTER amount")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_order_at INT(11) NOT NULL DEFAULT 0 AFTER end_restrict")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_leave_at INT(11) NOT NULL DEFAULT 0 AFTER last_order_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_delete_chats_at INT(11) NOT NULL DEFAULT 0 AFTER last_leave_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD api_id INT(11) DEFAULT NULL AFTER last_delete_chats_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD api_hash VARCHAR(50) DEFAULT NULL AFTER api_id")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD phone_code_hash varchar(100) DEFAULT NULL AFTER api_hash")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD code INT(11) DEFAULT NULL AFTER phone_code_hash")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD password varchar(100) DEFAULT NULL AFTER code")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD is_change_pass TINYINT(1) NOT NULL DEFAULT 0 AFTER password")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD change_pass_at INT(11) NOT NULL DEFAULT 0 AFTER is_change_pass")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD is_change_profile TINYINT(1) NOT NULL DEFAULT 0 AFTER change_pass_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD is_set_username TINYINT(1) NOT NULL DEFAULT 0 AFTER is_change_profile")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_update_status_at INT(11) NOT NULL DEFAULT 0 AFTER is_set_username")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_check_exit_at INT(11) NOT NULL DEFAULT 0 AFTER last_update_status_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_check_exit_count INT(11) NOT NULL DEFAULT 0 AFTER last_check_exit_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD last_del_pass_at INT(11) NOT NULL DEFAULT 0 AFTER last_check_exit_count")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD created_at INT(11) NOT NULL DEFAULT 0 AFTER last_del_pass_at")
alter_table(cs, f"ALTER TABLE {utl.mbots} ADD uniq_id VARCHAR(64) DEFAULT NULL AFTER created_at")


alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.cats} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.cats} ADD name varchar(50) DEFAULT NULL UNIQUE")
alter_table(cs, f"UPDATE {utl.mbots} SET cat_id=1 WHERE cat_id=0")

alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.countries} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD emoji varchar(50) DEFAULT NULL AFTER id")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD alpha_2 varchar(5) DEFAULT NULL AFTER emoji")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD name_fa varchar(50) DEFAULT NULL AFTER alpha_2")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD name_en varchar(50) DEFAULT NULL AFTER name_fa")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD area_code INT(11) NOT NULL DEFAULT 0 AFTER name_en")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD amount INT(11) NOT NULL DEFAULT 0 AFTER area_code")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD is_exists TINYINT(1) NOT NULL DEFAULT 1 AFTER amount")
alter_table(cs, f"ALTER TABLE {utl.countries} ADD is_useable TINYINT(1) NOT NULL DEFAULT 1 AFTER is_exists")


alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.users} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.users} ADD user_id BIGINT(20) DEFAULT NULL AFTER id")
alter_table(cs, f"ALTER TABLE {utl.users} ADD balance INT(11) NOT NULL DEFAULT 0 AFTER user_id")
alter_table(cs, f"ALTER TABLE {utl.users} ADD card VARCHAR(50) DEFAULT NULL AFTER balance")
alter_table(cs, f"ALTER TABLE {utl.users} ADD shaba VARCHAR(50) DEFAULT NULL AFTER card")
alter_table(cs, f"ALTER TABLE {utl.users} ADD status TINYINT(1) NOT NULL DEFAULT 0 AFTER shaba")
alter_table(cs, f"ALTER TABLE {utl.users} ADD step VARCHAR(128) DEFAULT NULL AFTER status")
alter_table(cs, f"ALTER TABLE {utl.users} ADD created_at INT(11) NOT NULL DEFAULT 0 AFTER step")
alter_table(cs, f"ALTER TABLE {utl.users} ADD uniq_id VARCHAR(64) DEFAULT NULL AFTER created_at")


alter_table(cs, f"CREATE TABLE IF NOT EXISTS {utl.withdrawal} (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD user_id BIGINT(20) DEFAULT NULL AFTER id")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD amount INT(11) NOT NULL DEFAULT 0 AFTER user_id")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD name VARCHAR(100) DEFAULT NULL AFTER amount")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD card VARCHAR(50) DEFAULT NULL AFTER name")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD shaba VARCHAR(50) DEFAULT NULL AFTER card")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD status TINYINT(1) NOT NULL DEFAULT 0 AFTER shaba")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD settled_at INT(11) NOT NULL DEFAULT 0 AFTER status")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD created_at INT(11) NOT NULL DEFAULT 0 AFTER settled_at")
alter_table(cs, f"ALTER TABLE {utl.withdrawal} ADD uniq_id VARCHAR(64) DEFAULT NULL AFTER created_at")

cs.execute(f"SELECT * FROM {utl.admin}")
row_admin = cs.fetchone()
if row_admin is None:
    cs.execute(f"INSERT INTO {utl.admin} (id) VALUES (1)")

cs.execute(f"SELECT * FROM {utl.cats}")
row_cats = cs.fetchone()
if row_cats is None:
    cs.execute(f"INSERT INTO {utl.cats} (id,name) VALUES (1,'default')")

try:
    cs.execute(f"""INSERT INTO {utl.countries} (id,emoji,alpha_2,name_fa,name_en,area_code,amount,is_exists,is_useable) VALUES
(1, '🇷🇺', 'ru', 'Russia', 'russia', 7, 5000, 1, 1),
(2, '🇺🇦', 'ua', 'Ukraine', 'ukraine', 380, 5000, 1, 1),
(3, '🇰🇿', 'kz', 'Kazakhstan', 'kazakhstan', 7, 5000, 1, 0),
(4, '🇨🇳', 'cn', 'China', 'china', 86, 5000, 1, 1),
(5, '🇵🇭', 'ph', 'Philippines', 'philippines', 63, 5000, 1, 1),
(6, '🇲🇲', 'mm', 'Myanmar', 'myanmar', 95, 5000, 1, 1),
(7, '🇮🇩', 'id', 'Indonesia', 'indonesia', 62, 5000, 1, 1),
(8, '🇲🇾', 'my', 'Malaysia', 'malaysia', 60, 5000, 1, 1),
(9, '🇰🇪', 'ke', 'kenya', 'kenya', 254, 5000, 1, 1),
(10, '🇹🇿', 'tz', 'Tanzania', 'tanzania', 255, 5000, 1, 1),
(11, '🇻🇳', 'vn', 'Vietnam', 'vietnam', 84, 5000, 1, 1),
(12, '🏴󠁧󠁢󠁥󠁮󠁿', 'gb', 'England', 'england', 44, 5000, 1, 1),
(13, '🇱🇻', 'lv', 'Latvia', 'latvia', 371, 5000, 1, 1),
(14, '🇷🇴', 'ro', 'Romania', 'romania', 40, 5000, 1, 1),
(15, '🇪🇪', 'ee', 'Estonia', 'estonia', 372, 5000, 1, 1),
(16, '🇺🇸', 'us', 'America', 'usa', 1, 5000, 1, 1),
(18, '🇰🇬', 'kg', 'Kyrgyzstan', 'kyrgyzstan', 996, 5000, 1, 1),
(19, '🇫🇷', 'fr', 'France', 'france', 33, 5000, 1, 1),
(21, '🇰🇭', 'kh', 'Cambodia', 'cambodia', 855, 5000, 1, 1),
(22, '🇲🇴', 'mo', 'Macau', 'macau', 853, 5000, 1, 1),
(24, '🇧🇷', 'br', 'Brazil', 'brazil', 55, 5000, 1, 1),
(25, '🇵🇱', 'pl', 'Poland', 'poland', 48, 5000, 1, 1),
(26, '🇵🇾', 'py', 'Paraguay', 'paraguay', 595, 5000, 1, 1),
(27, '🇳🇱', 'nl', 'Netherlands', 'netherlands', 31, 5000, 1, 1),
(28, '🇱🇹', 'lt', 'Lithuania', 'lithuania', 370, 5000, 1, 1),
(29, '🇲🇬', 'mg', 'Madagascar', 'madagascar', 261, 5000, 1, 1),
(30, '🇨🇩', 'cd', 'Congo', 'congo', 243, 5000, 1, 1),
(31, '🇳🇬', 'ng', 'Nigeria', 'nigeria', 234, 5000, 1, 1),
(32, '🇿🇦', 'za', 'South Africa', 'south africa', 27, 5000, 1, 1),
(33, '🇵🇦', 'pa', 'Panama', 'panama', 507, 5000, 1, 1),
(34, '🇪🇬', 'eg', 'Egypt', 20, 5000, 1, 1),
(35, '🇮🇳', 'in', 'India', 'india', 91, 5000, 1, 1),
(36, '🇮🇪', 'ie', 'Ireland', 'ireland', 353, 5000, 1, 1),
(37, '🇨🇮', 'ci', 'Ivory Coast', 'ivory coast', 225, 5000, 1, 1),
(39, '🇱🇦', 'la', 'Laos', 'laos', 856, 5000, 1, 1),
(40, '🇲🇦', 'ma', 'Morocco', 'morocco', 212, 5000, 1, 1),
(41, '🇾🇪', 'ye', 'Yemen', 'yemen', 967, 5000, 1, 1),
(42, '🇬🇭', 'gh', 'Ghana', 'ghana', 233, 5000, 1, 1),
(43, '🇨🇦', 'ca', 'Canada', 'canada', 1, 5000, 1, 0),
(44, '🇦🇷', 'ar', 'Argentina', 'argentina', 54, 5000, 1, 1),
(45, '🇮🇶', 'iq', 'iraq', 'iraq', 964, 5000, 1, 1),
(46, '🇩🇪', 'de', 'Germany', 'germany', 49, 5000, 1, 1),
(47, '🇨🇲', 'cm', 'Cameron', 'cameroon', 237, 5000, 1, 1),
(48, '🇹🇷', 'tr', 'Turkey', 'turkey', 90, 5000, 1, 1),
(49, '🇳🇿', 'nz', 'New Zealand', 'new zealand', 64, 5000, 1, 1),
(50, '🇦🇹', 'at', 'Austria', 'austria', 43, 5000, 1, 1),
(51, '🇸🇦', 'sa', 'Saudi Arabia', 'saudi arabia', 966, 5000, 1, 1),
(52, '🇲🇽', 'mx', 'Mexico', 'mexico', 52, 5000, 1, 1),
(53, '🇪🇸', 'es', 'Spain', 'spain', 34, 5000, 1, 1),
(54, '🇩🇿', 'dz', 'Algeria', 'algeria', 213, 5000, 1, 1),
(55, '🇸🇮', 'si', 'Slovenia', 'slovenia', 386, 5000, 1, 1),
(56, '🇭🇷', 'hr', 'Croatia', 'croatia', 385, 5000, 1, 1),
(57, '🇧🇾', 'by', 'Belarus', 'belarus', 375, 5000, 1, 1),
(58, '🇫🇮', 'fi', 'Finland', 'finland', 358, 5000, 1, 1),
(59, '🇸🇪', 'se', 'Sweden', 'sweden', 46, 5000, 1, 1),
(60, '🇬🇪', 'ge', 'Georgia', 'georgia', 995, 5000, 1, 1),
(61, '🇪🇹', 'et', 'Ethiopia', 'ethiopia', 251, 5000, 1, 1),
(62, '🇿🇲', 'zm', 'Zambia', 'zambia', 260, 5000, 1, 1),
(63, '🇵🇰', 'pk', 'Pakistan', 'pakistan', 92, 5000, 1, 1),
(64, '🇹🇭', 'th', 'Thailand', 'thailand', 66, 5000, 1, 1),
(65, '🇹🇼', 'tw', 'Taiwan', 'taiwan', 886, 5000, 1, 1),
(66, '🇵🇪', 'pe', 'Peru', 'peru', 51, 5000, 1, 1),
(68, '🇹🇩', 'td', 'Chad', 'chad', 235, 5000, 1, 1),
(69, '🇲🇱', 'ml', 'Mali', 'mali', 223, 5000, 1, 1),
(70, '🇧🇩', 'bd', 'Bangladesh', 'bangladesh', 880, 5000, 1, 1),
(71, '🇬🇳', 'gn', 'Guinea', 'guinea', 224, 5000, 1, 1),
(72, '🇱🇰', 'lk', 'Sri Lanka', 'sri lanka', 94, 5000, 1, 1),
(73, '🇺🇿', 'uz', 'Uzbekistan', 'uzbekistan', 998, 5000, 1, 1),
(74, '🇸🇳', 'sn', 'Senegal', 'senegal', 221, 5000, 1, 1),
(75, '🇨🇴', 'co', 'Colombia', 'colombia', 57, 5000, 1, 1),
(76, '🇻🇪', 've', 'Venezuela', 'venezuela', 58, 5000, 1, 1),
(77, '🇭🇹', 'ht', 'Haiti', 'haiti', 509, 5000, 1, 1),
(78, '🇮🇷', 'ir', 'Iran', 'iran', 98, 5000, 1, 1),
(79, '🇲🇩', 'md', 'Moldova', 'moldova', 373, 5000, 1, 1),
(80, '🇲🇿', 'mz', 'Mozambique', 'mozambique', 258, 5000, 1, 1),
(82, '🇦🇫', 'af', 'Afghanistan', 'afghanistan', 93, 5000, 1, 1),
(83, '🇺🇬', 'ug', 'Uganda', 'uganda', 256, 5000, 1, 1),
(84, '🇦🇺', 'au', 'Australia', 'australia', 61, 5000, 1, 1),
(85, '🇦🇪', 'ae', 'UAE', 'uae', 971, 5000, 1, 1),
(86, '🇨🇱', 'cl', 'Chile', 'chile', 56, 5000, 1, 1),
(88, '🇳🇵', 'np', 'Nepal', 'nepal', 977, 5000, 1, 1),
(89, '🇩🇯', 'dj', 'Djibouti', 'djibouti', 253, 5000, 1, 1),
(91, '🇳🇮', 'ni', 'Nicaragua', 'nicaragua', 505, 5000, 1, 1),
(94, '🇦🇴', 'ao', 'Angola', 'angola', 244, 5000, 1, 1),
(95, '🇧🇴', 'bo', 'Bolivia', 'bolivia', 591, 5000, 1, 1),
(96, '🇺🇾', 'uy', 'Uruguay', 'uruguay', 598, 5000, 1, 1),
(97, '🇪🇨', 'ec', 'Ecuador', 'ecuador', 593, 5000, 1, 1),
(98, '🇮🇹', 'it', 'Italia', 'italy', 39, 5000, 1, 1),
(99, '🇬🇹', 'gt', 'Guatemala', 'guatemala', 502, 5000, 1, 1),
(100, '🇹🇳', 'tn', 'Tunisia', 'tunisia', 216, 5000, 1, 1),
(101, '🇭🇺', 'hu', 'Hungary', 'hungary', 36, 5000, 1, 1),
(102, '🇰🇼', 'kw', 'Kuwait', 'kuwait', 965, 5000, 1, 1),
(103, '🇦🇿', 'az', 'Azerbaijan', 'azerbaijan', 994, 5000, 1, 1),
(104, '🇸🇩', 'sd', 'Sudan', 'sudan', 249, 5000, 1, 1),
(105, '🇷🇼', 'rw', 'Rwanda', 'rwanda', 250, 5000, 1, 1),
(108, '🇨🇷', 'cr', 'Costa Rica', 'costa rica', 506, 5000, 1, 1),
(109, '🇭🇳', 'hn', 'Honduras', 'honduras', 504, 5000, 1, 1),
(113, '🇹🇲', 'tm', 'Turkmenistan', 'turkmenistan', 993, 5000, 1, 1),
(114, '🇸🇾', 'sy', 'Syria', 'syria', 963, 5000, 1, 1),
(117, '🇵🇷', 'pr', 'Puerto Rico', 'puerto rico', 1, 5000, 1, 0),
(118, '🇧🇬', 'bg', 'Bulgaria', 'bulgaria', 359, 5000, 0, 1),
(119, '🇧🇪', 'be', 'Belgium', 'belgium', 32, 5000, 1, 1),
(120, '🇨🇿', 'cz', 'Czech', 'czech', 420, 5000, 1, 1),
(121, '🇸🇰', 'sk', 'Slovakia', 'slovakia', 421, 5000, 1, 1),
(122, '🇳🇴', 'no', 'Norway', 'norway', 47, 5000, 1, 1),
(123, '🇵🇹', 'pt', 'Portugal', 'portugal', 351, 5000, 1, 1),
(124, '🇱🇺', 'lu', 'Luxembourg', 'luxembourg', 352, 5000, 1, 1),
(125, '🇦🇲', 'am', 'Armenia', 'armenia', 374, 5000, 1, 1),
(126, '🇯🇲', 'jm', 'Jamaica', 'jamaica', 1876, 5000, 1, 1),
(129, '🇯🇴', 'jo', 'Jordan', 'jordan', 962, 5000, 1, 1),
(130, '🇴🇲', 'om', 'Oman', 'oman', 968, 5000, 1, 1),
(131, '🇧🇭', 'bh', 'Bahrain', 'bahrain', 973, 5000, 1, 1),
(132, '🇶🇦', 'qa', 'Qatar', 'qatar', 974, 5000, 1, 1),
(133, '🇲🇳', 'mn', 'Mongolia', 'mongolia', 976, 5000, 1, 1),
(134, '🇲🇻', 'mv', 'Maldives', 'maldives', 960, 5000, 1, 1),
(135, '🇱🇾', 'ly', 'Libya', 'libya', 218, 5000, 1, 1),
(137, '🇧🇫', 'bf', 'Burkina Faso', 'burkina faso', 226, 5000, 1, 1),
(139, '🇧🇯', 'bj', 'Benin', 'benin', 229, 5000, 1, 1),
(141, '🇸🇴', 'so', 'Somalia', 'somalia', 252, 5000, 0, 1),
(142, '🇿🇼', 'zw', 'Zimbabwe', 'zimbabwe', 263, 5000, 1, 1),
(148, '🇨🇭', 'ch', 'Switzerland', 'switzerland', 41, 5000, 0, 1),
(150, '🇧🇧', 'bb', 'Barbados', 'barbados', 1246, 5000, 0, 1),
(155, '🇸🇬', 'sg', 'Singapore', 'singapore', 65, 5000, 1, 1),
(156, '🇹🇯', 'tj', 'Tajikistan', 'tajikistan', 992, 5000, 0, 1),
(159, '🇨🇾', 'cy', 'Cyprus', 'cyprus', 357, 5000, 0, 1);""")

except:
    pass