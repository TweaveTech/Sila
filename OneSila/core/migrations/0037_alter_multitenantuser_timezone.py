# Generated by Django 5.0.2 on 2024-04-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Europe/London', 'Europe/London'), ('America/Curacao', 'America/Curacao'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Africa/Kampala', 'Africa/Kampala'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Indianapolis', 'America/Indianapolis'), ('America/Toronto', 'America/Toronto'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/Rosario', 'America/Rosario'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Europe/Bucharest', 'Europe/Bucharest'), ('GB', 'GB'), ('Asia/Vientiane', 'Asia/Vientiane'), ('America/Noronha', 'America/Noronha'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Africa/Bissau', 'Africa/Bissau'), ('MST', 'MST'), ('Pacific/Palau', 'Pacific/Palau'), ('Navajo', 'Navajo'), ('America/Menominee', 'America/Menominee'), ('Poland', 'Poland'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Pacific/Wake', 'Pacific/Wake'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/St_Kitts', 'America/St_Kitts'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Australia/Victoria', 'Australia/Victoria'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Tehran', 'Asia/Tehran'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Caracas', 'America/Caracas'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/Belize', 'America/Belize'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Europe/Jersey', 'Europe/Jersey'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Ensenada', 'America/Ensenada'), ('Indian/Christmas', 'Indian/Christmas'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Indian/Mahe', 'Indian/Mahe'), ('Europe/Riga', 'Europe/Riga'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Marigot', 'America/Marigot'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Africa/Douala', 'Africa/Douala'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Pacific/Easter', 'Pacific/Easter'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Australia/North', 'Australia/North'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Europe/Prague', 'Europe/Prague'), ('GMT-0', 'GMT-0'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('US/Alaska', 'US/Alaska'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Iqaluit', 'America/Iqaluit'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Europe/Madrid', 'Europe/Madrid'), ('Africa/Lagos', 'Africa/Lagos'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Asia/Hebron', 'Asia/Hebron'), ('Asia/Taipei', 'Asia/Taipei'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Africa/Lome', 'Africa/Lome'), ('Asia/Muscat', 'Asia/Muscat'), ('America/Cordoba', 'America/Cordoba'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Pacific/Yap', 'Pacific/Yap'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Chongqing', 'Asia/Chongqing'), ('America/Virgin', 'America/Virgin'), ('America/Belem', 'America/Belem'), ('Europe/Monaco', 'Europe/Monaco'), ('America/Cancun', 'America/Cancun'), ('Asia/Aden', 'Asia/Aden'), ('UCT', 'UCT'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Grenada', 'America/Grenada'), ('America/Catamarca', 'America/Catamarca'), ('America/Cayenne', 'America/Cayenne'), ('Africa/Accra', 'Africa/Accra'), ('Australia/Currie', 'Australia/Currie'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Havana', 'America/Havana'), ('Asia/Calcutta', 'Asia/Calcutta'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('EST5EDT', 'EST5EDT'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Kabul', 'Asia/Kabul'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('GB-Eire', 'GB-Eire'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Africa/Maputo', 'Africa/Maputo'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('ROK', 'ROK'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Inuvik', 'America/Inuvik'), ('Asia/Makassar', 'Asia/Makassar'), ('Europe/Busingen', 'Europe/Busingen'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Jamaica', 'Jamaica'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Maceio', 'America/Maceio'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Winnipeg', 'America/Winnipeg'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('America/St_Vincent', 'America/St_Vincent'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Bahia', 'America/Bahia'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Thule', 'America/Thule'), ('Europe/Paris', 'Europe/Paris'), ('Asia/Macao', 'Asia/Macao'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Barbados', 'America/Barbados'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Africa/Harare', 'Africa/Harare'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Baku', 'Asia/Baku'), ('America/Adak', 'America/Adak'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Yangon', 'Asia/Yangon'), ('Canada/Pacific', 'Canada/Pacific'), ('US/Mountain', 'US/Mountain'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Colombo', 'Asia/Colombo'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Santarem', 'America/Santarem'), ('HST', 'HST'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Yakutat', 'America/Yakutat'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Creston', 'America/Creston'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Africa/Gaborone', 'Africa/Gaborone'), ('America/Halifax', 'America/Halifax'), ('America/Jamaica', 'America/Jamaica'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Etc/GMT+9', 'Etc/GMT+9'), ('US/Samoa', 'US/Samoa'), ('GMT0', 'GMT0'), ('Pacific/Truk', 'Pacific/Truk'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Oral', 'Asia/Oral'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Asia/Damascus', 'Asia/Damascus'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Europe/Podgorica', 'Europe/Podgorica'), ('America/Matamoros', 'America/Matamoros'), ('Asia/Singapore', 'Asia/Singapore'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('US/Arizona', 'US/Arizona'), ('Iran', 'Iran'), ('America/Juneau', 'America/Juneau'), ('Europe/Belfast', 'Europe/Belfast'), ('Asia/Dili', 'Asia/Dili'), ('America/Regina', 'America/Regina'), ('Africa/Juba', 'Africa/Juba'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Tijuana', 'America/Tijuana'), ('America/Atikokan', 'America/Atikokan'), ('US/Eastern', 'US/Eastern'), ('Etc/GMT-12', 'Etc/GMT-12'), ('America/Tortola', 'America/Tortola'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Universal', 'Universal'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Asuncion', 'America/Asuncion'), ('America/Guyana', 'America/Guyana'), ('Africa/Algiers', 'Africa/Algiers'), ('Brazil/West', 'Brazil/West'), ('America/Cayman', 'America/Cayman'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Canada/Central', 'Canada/Central'), ('Australia/Eucla', 'Australia/Eucla'), ('Europe/Malta', 'Europe/Malta'), ('Africa/Libreville', 'Africa/Libreville'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Brazil/Acre', 'Brazil/Acre'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Chile/Continental', 'Chile/Continental'), ('Etc/UTC', 'Etc/UTC'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Montevideo', 'America/Montevideo'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('US/Pacific', 'US/Pacific'), ('Africa/Bamako', 'Africa/Bamako'), ('Australia/South', 'Australia/South'), ('America/Guayaquil', 'America/Guayaquil'), ('Asia/Kuching', 'Asia/Kuching'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Australia/Canberra', 'Australia/Canberra'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Asia/Brunei', 'Asia/Brunei'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Europe/Kiev', 'Europe/Kiev'), ('PRC', 'PRC'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/Boise', 'America/Boise'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Kwajalein', 'Kwajalein'), ('Asia/Saigon', 'Asia/Saigon'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Managua',
                                   'America/Managua'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Asia/Chungking', 'Asia/Chungking'), ('America/New_York', 'America/New_York'), ('Europe/Athens', 'Europe/Athens'), ('America/Rainy_River', 'America/Rainy_River'), ('Asia/Baghdad', 'Asia/Baghdad'), ('CET', 'CET'), ('America/Mazatlan', 'America/Mazatlan'), ('US/Hawaii', 'US/Hawaii'), ('America/Montreal', 'America/Montreal'), ('America/Guatemala', 'America/Guatemala'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Australia/ACT', 'Australia/ACT'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Africa/Asmera', 'Africa/Asmera'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Europe/Rome', 'Europe/Rome'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Martinique', 'America/Martinique'), ('GMT+0', 'GMT+0'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Aruba', 'America/Aruba'), ('Australia/Queensland', 'Australia/Queensland'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Etc/Zulu', 'Etc/Zulu'), ('Egypt', 'Egypt'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Etc/GMT-3', 'Etc/GMT-3'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Australia/Perth', 'Australia/Perth'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('America/Chicago', 'America/Chicago'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Asia/Magadan', 'Asia/Magadan'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('US/Michigan', 'US/Michigan'), ('Europe/Minsk', 'Europe/Minsk'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Detroit', 'America/Detroit'), ('America/Monterrey', 'America/Monterrey'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Canada/Mountain', 'Canada/Mountain'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Etc/GMT0', 'Etc/GMT0'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Shiprock', 'America/Shiprock'), ('Hongkong', 'Hongkong'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Fortaleza', 'America/Fortaleza'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Australia/LHI', 'Australia/LHI'), ('Europe/Saratov', 'Europe/Saratov'), ('Australia/Hobart', 'Australia/Hobart'), ('Asia/Qatar', 'Asia/Qatar'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Harbin', 'Asia/Harbin'), ('Africa/Freetown', 'Africa/Freetown'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Macau', 'Asia/Macau'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Japan', 'Japan'), ('EET', 'EET'), ('America/Anguilla', 'America/Anguilla'), ('America/Bogota', 'America/Bogota'), ('CST6CDT', 'CST6CDT'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Iceland', 'Iceland'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Jujuy', 'America/Jujuy'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Europe/Dublin', 'Europe/Dublin'), ('America/Dawson', 'America/Dawson'), ('America/Mendoza', 'America/Mendoza'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Manaus', 'America/Manaus'), ('Cuba', 'Cuba'), ('America/Atka', 'America/Atka'), ('Europe/Moscow', 'Europe/Moscow'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Indian/Maldives', 'Indian/Maldives'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Nome', 'America/Nome'), ('America/Antigua', 'America/Antigua'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Australia/West', 'Australia/West'), ('Europe/Brussels', 'Europe/Brussels'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Pacific/Midway', 'Pacific/Midway'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Almaty', 'Asia/Almaty'), ('America/St_Thomas', 'America/St_Thomas'), ('America/Sitka', 'America/Sitka'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Panama', 'America/Panama'), ('America/Moncton', 'America/Moncton'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Africa/Conakry', 'Africa/Conakry'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('PST8PDT', 'PST8PDT'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Gaza', 'Asia/Gaza'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('ROC', 'ROC'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Pacific/Guam', 'Pacific/Guam'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Santiago', 'America/Santiago'), ('NZ-CHAT', 'NZ-CHAT'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Indian/Comoro', 'Indian/Comoro'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/El_Salvador', 'America/El_Salvador'), ('MST7MDT', 'MST7MDT'), ('Africa/Malabo', 'Africa/Malabo'), ('Australia/Sydney', 'Australia/Sydney'), ('NZ', 'NZ'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Etc/GMT+1', 'Etc/GMT+1'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('America/Recife', 'America/Recife'), ('Australia/NSW', 'Australia/NSW'), ('Factory', 'Factory'), ('America/Dominica', 'America/Dominica'), ('America/Resolute', 'America/Resolute'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Asia/Hovd', 'Asia/Hovd'), ('America/Merida', 'America/Merida'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('Portugal', 'Portugal'), ('Africa/Asmara', 'Africa/Asmara'), ('Israel', 'Israel'), ('Antarctica/Casey', 'Antarctica/Casey'), ('America/Miquelon', 'America/Miquelon'), ('Pacific/Niue', 'Pacific/Niue'), ('America/Montserrat', 'America/Montserrat'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Libya', 'Libya'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Vancouver', 'America/Vancouver'), ('Etc/UCT', 'Etc/UCT'), ('Africa/Niamey', 'Africa/Niamey'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Turkey', 'Turkey'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Canada/Eastern', 'Canada/Eastern'), ('America/St_Lucia', 'America/St_Lucia'), ('Eire', 'Eire'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Campo_Grande', 'America/Campo_Grande'), ('America/Knox_IN', 'America/Knox_IN'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Europe/Tirane', 'Europe/Tirane'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('America/Lima', 'America/Lima'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Metlakatla', 'America/Metlakatla'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Chita', 'Asia/Chita'), ('Greenwich', 'Greenwich'), ('America/Eirunepe', 'America/Eirunepe'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Zulu', 'Zulu'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Europe/Vatican', 'Europe/Vatican'), ('America/Yellowknife', 'America/Yellowknife'), ('Pacific/Efate', 'Pacific/Efate'), ('America/Ojinaga', 'America/Ojinaga'), ('Asia/Barnaul', 'Asia/Barnaul'), ('MET', 'MET'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Godthab', 'America/Godthab'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/La_Paz', 'America/La_Paz'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Etc/GMT-11', 'Etc/GMT-11'), ('UTC', 'UTC'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Brazil/East', 'Brazil/East'), ('Asia/Manila', 'Asia/Manila'), ('America/Guadeloupe', 'America/Guadeloupe'), ('US/Central', 'US/Central'), ('US/East-Indiana', 'US/East-Indiana'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Africa/Kigali', 'Africa/Kigali'), ('Europe/Vienna', 'Europe/Vienna'), ('Mexico/General', 'Mexico/General'), ('WET', 'WET'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('America/Paramaribo', 'America/Paramaribo'), ('build/etc/localtime', 'build/etc/localtime'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Africa/Maseru', 'Africa/Maseru'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Australia/Darwin', 'Australia/Darwin'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Jakarta', 'Asia/Jakarta'), ('GMT', 'GMT'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/St_Johns', 'America/St_Johns'), ('America/Denver', 'America/Denver'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('EST', 'EST'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Asia/Dacca', 'Asia/Dacca'), ('Canada/Yukon', 'Canada/Yukon'), ('America/Louisville', 'America/Louisville'), ('Africa/Cairo', 'Africa/Cairo'), ('W-SU', 'W-SU'), ('Singapore', 'Singapore'), ('Europe/Samara', 'Europe/Samara'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Araguaina', 'America/Araguaina'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Europe/Budapest', 'Europe/Budapest'), ('Indian/Chagos', 'Indian/Chagos'), ('America/Nassau', 'America/Nassau'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Anchorage', 'America/Anchorage'), ('Asia/Beirut', 'Asia/Beirut'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Etc/GMT+6', 'Etc/GMT+6'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('US/Aleutian', 'US/Aleutian'), ('Antarctica/Syowa', 'Antarctica/Syowa')], default='Europe/London', max_length=35),
        ),
    ]
