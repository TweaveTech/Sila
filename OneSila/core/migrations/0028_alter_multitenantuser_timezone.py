# Generated by Django 5.0.2 on 2024-03-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_multitenantcompany_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Anguilla', 'America/Anguilla'), ('Europe/Saratov', 'Europe/Saratov'), ('America/Belize', 'America/Belize'), ('Africa/Lome', 'Africa/Lome'), ('Pacific/Yap', 'Pacific/Yap'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Magadan', 'Asia/Magadan'), ('Etc/GMT+2', 'Etc/GMT+2'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Creston', 'America/Creston'), ('Brazil/West', 'Brazil/West'), ('Africa/Nairobi', 'Africa/Nairobi'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Nuuk', 'America/Nuuk'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Managua', 'America/Managua'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Prague', 'Europe/Prague'), ('Asia/Manila', 'Asia/Manila'), ('America/Cuiaba', 'America/Cuiaba'), ('US/Hawaii', 'US/Hawaii'), ('America/Knox_IN', 'America/Knox_IN'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Recife', 'America/Recife'), ('Asia/Saigon', 'Asia/Saigon'), ('Indian/Christmas', 'Indian/Christmas'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Hongkong', 'Hongkong'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Europe/Helsinki', 'Europe/Helsinki'), ('PRC', 'PRC'), ('America/Atka', 'America/Atka'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Etc/GMT-5', 'Etc/GMT-5'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Africa/Kampala', 'Africa/Kampala'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Martinique', 'America/Martinique'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Gaza', 'Asia/Gaza'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Maceio', 'America/Maceio'), ('Africa/Malabo', 'Africa/Malabo'), ('Asia/Beirut', 'Asia/Beirut'), ('Pacific/Truk', 'Pacific/Truk'), ('Asia/Baku', 'Asia/Baku'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('ROK', 'ROK'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Europe/Busingen', 'Europe/Busingen'), ('America/Mazatlan', 'America/Mazatlan'), ('Europe/Monaco', 'Europe/Monaco'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Cuba', 'Cuba'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Noronha', 'America/Noronha'), ('Canada/Atlantic', 'Canada/Atlantic'), ('America/Guayaquil', 'America/Guayaquil'), ('Egypt', 'Egypt'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('US/Alaska', 'US/Alaska'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Etc/GMT+0', 'Etc/GMT+0'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('US/Arizona', 'US/Arizona'), ('Zulu', 'Zulu'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Atikokan', 'America/Atikokan'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Asia/Riyadh', 'Asia/Riyadh'), ('MST', 'MST'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Israel', 'Israel'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Indian/Mahe', 'Indian/Mahe'), ('Africa/Gaborone', 'Africa/Gaborone'), ('GMT', 'GMT'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Europe/Vienna', 'Europe/Vienna'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/Jujuy', 'America/Jujuy'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Indian/Maldives', 'Indian/Maldives'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Africa/Kigali', 'Africa/Kigali'), ('America/Halifax', 'America/Halifax'), ('America/Thule', 'America/Thule'), ('America/Boise', 'America/Boise'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Juneau', 'America/Juneau'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Nipigon', 'America/Nipigon'), ('Indian/Cocos', 'Indian/Cocos'), ('UCT', 'UCT'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Merida', 'America/Merida'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Pacific/Niue', 'Pacific/Niue'), ('Australia/NSW', 'Australia/NSW'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Kuching', 'Asia/Kuching'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Detroit', 'America/Detroit'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Africa/Algiers', 'Africa/Algiers'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Asia/Aqtau', 'Asia/Aqtau'), ('HST', 'HST'), ('Portugal', 'Portugal'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/St_Johns', 'America/St_Johns'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Asia/Colombo', 'Asia/Colombo'), ('Greenwich', 'Greenwich'), ('US/Michigan', 'US/Michigan'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Cancun', 'America/Cancun'), ('Asia/Muscat', 'Asia/Muscat'), ('Asia/Yangon', 'Asia/Yangon'), ('Asia/Makassar', 'Asia/Makassar'), ('Europe/London', 'Europe/London'), ('Australia/Canberra', 'Australia/Canberra'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Africa/Maputo', 'Africa/Maputo'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Brazil/Acre', 'Brazil/Acre'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Africa/Niamey', 'Africa/Niamey'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Ojinaga', 'America/Ojinaga'), ('MST7MDT', 'MST7MDT'), ('Africa/Dakar', 'Africa/Dakar'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Mexico_City', 'America/Mexico_City'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Europe/Paris', 'Europe/Paris'), ('America/Monterrey', 'America/Monterrey'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Swift_Current', 'America/Swift_Current'), ('Europe/Stockholm', 'Europe/Stockholm'), ('GMT0', 'GMT0'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Metlakatla', 'America/Metlakatla'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Adak', 'America/Adak'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Australia/LHI', 'Australia/LHI'), ('Kwajalein', 'Kwajalein'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/St_Kitts', 'America/St_Kitts'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('US/East-Indiana', 'US/East-Indiana'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Eire', 'Eire'), ('America/Yakutat', 'America/Yakutat'), ('America/Virgin', 'America/Virgin'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Belem', 'America/Belem'), ('Asia/Qatar', 'Asia/Qatar'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Australia/Eucla', 'Australia/Eucla'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Macao', 'Asia/Macao'), ('Asia/Harbin', 'Asia/Harbin'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Africa/Douala', 'Africa/Douala'), ('America/Antigua', 'America/Antigua'), ('America/Menominee', 'America/Menominee'), ('America/Nassau', 'America/Nassau'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('US/Aleutian', 'US/Aleutian'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('NZ', 'NZ'), ('Turkey', 'Turkey'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Dawson', 'America/Dawson'), ('Singapore', 'Singapore'), ('Africa/Accra', 'Africa/Accra'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Indian/Reunion', 'Indian/Reunion'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Etc/GMT-7', 'Etc/GMT-7'), ('US/Mountain', 'US/Mountain'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Europe/Skopje', 'Europe/Skopje'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Asia/Aden', 'Asia/Aden'), ('Asia/Almaty', 'Asia/Almaty'), ('Asia/Dubai', 'Asia/Dubai'), ('Pacific/Midway', 'Pacific/Midway'), ('Canada/Eastern', 'Canada/Eastern'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Europe/Riga', 'Europe/Riga'), ('US/Pacific', 'US/Pacific'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Universal', 'Universal'), ('America/Guyana', 'America/Guyana'), ('Atlantic/Azores', 'Atlantic/Azores'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Toronto', 'America/Toronto'), ('Europe/Simferopol', 'Europe/Simferopol'), ('America/New_York', 'America/New_York'), ('ROC', 'ROC'), ('Africa/Lagos', 'Africa/Lagos'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Pacific/Apia', 'Pacific/Apia'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Sitka', 'America/Sitka'), ('Australia/Perth', 'Australia/Perth'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Brazil/East', 'Brazil/East'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Australia/Sydney', 'Australia/Sydney'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'),
                                   ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Miquelon', 'America/Miquelon'), ('PST8PDT', 'PST8PDT'), ('America/Manaus', 'America/Manaus'), ('Africa/Libreville', 'Africa/Libreville'), ('Etc/UCT', 'Etc/UCT'), ('America/Rosario', 'America/Rosario'), ('Mexico/General', 'Mexico/General'), ('UTC', 'UTC'), ('Etc/Universal', 'Etc/Universal'), ('America/Montserrat', 'America/Montserrat'), ('America/Curacao', 'America/Curacao'), ('Asia/Macau', 'Asia/Macau'), ('Japan', 'Japan'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Amman', 'Asia/Amman'), ('America/St_Thomas', 'America/St_Thomas'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('America/Panama', 'America/Panama'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Asuncion', 'America/Asuncion'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Navajo', 'Navajo'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Inuvik', 'America/Inuvik'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Bahia', 'America/Bahia'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Asia/Kabul', 'Asia/Kabul'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Iceland', 'Iceland'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Hebron', 'Asia/Hebron'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Africa/Juba', 'Africa/Juba'), ('America/Lima', 'America/Lima'), ('Australia/South', 'Australia/South'), ('America/Regina', 'America/Regina'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Europe/Athens', 'Europe/Athens'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Canada/Mountain', 'Canada/Mountain'), ('America/Nome', 'America/Nome'), ('Europe/Kirov', 'Europe/Kirov'), ('Iran', 'Iran'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Australia/Darwin', 'Australia/Darwin'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Grenada', 'America/Grenada'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Canada/Central', 'Canada/Central'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Europe/Jersey', 'Europe/Jersey'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Shiprock', 'America/Shiprock'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Bogota', 'America/Bogota'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Tortola', 'America/Tortola'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Antarctica/Casey', 'Antarctica/Casey'), ('America/Moncton', 'America/Moncton'), ('America/Anchorage', 'America/Anchorage'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Africa/Cairo', 'Africa/Cairo'), ('US/Eastern', 'US/Eastern'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Dominica', 'America/Dominica'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Aruba', 'America/Aruba'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Australia/West', 'Australia/West'), ('America/Whitehorse', 'America/Whitehorse'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Australia/Victoria', 'Australia/Victoria'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Africa/Abidjan', 'Africa/Abidjan'), ('MET', 'MET'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Asia/Brunei', 'Asia/Brunei'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Damascus', 'Asia/Damascus'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Canada/Yukon', 'Canada/Yukon'), ('Australia/North', 'Australia/North'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Taipei', 'Asia/Taipei'), ('America/Matamoros', 'America/Matamoros'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Jamaica', 'Jamaica'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Australia/Queensland', 'Australia/Queensland'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Cayman', 'America/Cayman'), ('Pacific/Easter', 'Pacific/Easter'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Belfast', 'Europe/Belfast'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('America/Ensenada', 'America/Ensenada'), ('America/El_Salvador', 'America/El_Salvador'), ('Europe/Minsk', 'Europe/Minsk'), ('US/Central', 'US/Central'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Chita', 'Asia/Chita'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/La_Paz', 'America/La_Paz'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Europe/Rome', 'Europe/Rome'), ('GB-Eire', 'GB-Eire'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Montevideo', 'America/Montevideo'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('US/Samoa', 'US/Samoa'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Cordoba', 'America/Cordoba'), ('Pacific/Palau', 'Pacific/Palau'), ('America/Kralendijk', 'America/Kralendijk'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Eirunepe', 'America/Eirunepe'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Marigot', 'America/Marigot'), ('GMT+0', 'GMT+0'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Pacific/Guam', 'Pacific/Guam'), ('Chile/Continental', 'Chile/Continental'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Asia/Dili', 'Asia/Dili'), ('America/Caracas', 'America/Caracas'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Godthab', 'America/Godthab'), ('Europe/Zurich', 'Europe/Zurich'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Libya', 'Libya'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Edmonton', 'America/Edmonton'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Africa/Harare', 'Africa/Harare'), ('Etc/UTC', 'Etc/UTC'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Pacific/Wake', 'Pacific/Wake'), ('Europe/Tirane', 'Europe/Tirane'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Mendoza', 'America/Mendoza'), ('WET', 'WET'), ('Europe/Samara', 'Europe/Samara'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Rainy_River', 'America/Rainy_River'), ('Africa/Freetown', 'Africa/Freetown'), ('Asia/Dacca', 'Asia/Dacca'), ('EST', 'EST'), ('Europe/Madrid', 'Europe/Madrid'), ('Indian/Chagos', 'Indian/Chagos'), ('Australia/Currie', 'Australia/Currie'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Araguaina', 'America/Araguaina'), ('Europe/Malta', 'Europe/Malta'), ('America/Catamarca', 'America/Catamarca'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Factory', 'Factory'), ('Africa/Windhoek', 'Africa/Windhoek'), ('GB', 'GB'), ('America/Tijuana', 'America/Tijuana'), ('America/Montreal', 'America/Montreal'), ('America/Louisville', 'America/Louisville'), ('EST5EDT', 'EST5EDT'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Resolute', 'America/Resolute'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Santarem', 'America/Santarem'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/St_Lucia', 'America/St_Lucia'), ('Europe/Kiev', 'Europe/Kiev'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('GMT-0', 'GMT-0'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('W-SU', 'W-SU'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Australia/Tasmania', 'Australia/Tasmania'), ('EET', 'EET'), ('America/Santiago', 'America/Santiago'), ('America/Guatemala', 'America/Guatemala'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Africa/Asmara', 'Africa/Asmara'), ('Australia/ACT', 'Australia/ACT'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('America/Chicago', 'America/Chicago'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Conakry', 'Africa/Conakry'), ('Europe/Sofia', 'Europe/Sofia'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Africa/Banjul', 'Africa/Banjul'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('America/Fortaleza', 'America/Fortaleza'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Vancouver', 'America/Vancouver'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Canada/Pacific', 'Canada/Pacific'), ('Pacific/Efate', 'Pacific/Efate'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('America/Cayenne', 'America/Cayenne'), ('America/Yellowknife', 'America/Yellowknife'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('CST6CDT', 'CST6CDT'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Denver', 'America/Denver'), ('CET', 'CET'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/Barbados', 'America/Barbados'), ('America/Jamaica', 'America/Jamaica'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Poland', 'Poland'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Australia/Hobart', 'Australia/Hobart'), ('America/Havana', 'America/Havana'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Singapore', 'Asia/Singapore')], default='Europe/London', max_length=35),
        ),
    ]
