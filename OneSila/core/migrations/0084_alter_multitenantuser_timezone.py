# Generated by Django 5.0.2 on 2024-06-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Asia/Dili', 'Asia/Dili'), ('EST5EDT', 'EST5EDT'), ('America/Resolute', 'America/Resolute'), ('Asia/Omsk', 'Asia/Omsk'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('America/Swift_Current', 'America/Swift_Current'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Europe/Dublin', 'Europe/Dublin'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Australia/ACT', 'Australia/ACT'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Seoul', 'Asia/Seoul'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Europe/Minsk', 'Europe/Minsk'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Phoenix', 'America/Phoenix'), ('PST8PDT', 'PST8PDT'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/Havana', 'America/Havana'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Jujuy', 'America/Jujuy'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Australia/South', 'Australia/South'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Europe/Skopje', 'Europe/Skopje'), ('America/La_Paz', 'America/La_Paz'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Canada/Eastern', 'Canada/Eastern'), ('America/Bogota', 'America/Bogota'), ('America/Louisville', 'America/Louisville'), ('CET', 'CET'), ('America/Cancun', 'America/Cancun'), ('Europe/Paris', 'Europe/Paris'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('NZ', 'NZ'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Africa/Douala', 'Africa/Douala'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('US/Aleutian', 'US/Aleutian'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Asia/Hebron', 'Asia/Hebron'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('US/Central', 'US/Central'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Toronto', 'America/Toronto'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Australia/Perth', 'Australia/Perth'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/Edmonton', 'America/Edmonton'), ('Indian/Maldives', 'Indian/Maldives'), ('Australia/Darwin', 'Australia/Darwin'), ('Brazil/East', 'Brazil/East'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Indian/Chagos', 'Indian/Chagos'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Pacific/Niue', 'Pacific/Niue'), ('US/Mountain', 'US/Mountain'), ('Indian/Christmas', 'Indian/Christmas'), ('Zulu', 'Zulu'), ('Australia/LHI', 'Australia/LHI'), ('US/Samoa', 'US/Samoa'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Nome', 'America/Nome'), ('America/Cayenne', 'America/Cayenne'), ('Factory', 'Factory'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Asia/Tehran', 'Asia/Tehran'), ('Pacific/Wake', 'Pacific/Wake'), ('Asia/Dacca', 'Asia/Dacca'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Grenada', 'America/Grenada'), ('Asia/Gaza', 'Asia/Gaza'), ('ROC', 'ROC'), ('America/Ensenada', 'America/Ensenada'), ('America/Rainy_River', 'America/Rainy_River'), ('Asia/Baku', 'Asia/Baku'), ('America/Jamaica', 'America/Jamaica'), ('Europe/Zurich', 'Europe/Zurich'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Australia/Queensland', 'Australia/Queensland'), ('America/Bahia', 'America/Bahia'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Europe/Madrid', 'Europe/Madrid'), ('Portugal', 'Portugal'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Nassau', 'America/Nassau'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Manaus', 'America/Manaus'), ('Etc/GMT-4', 'Etc/GMT-4'), ('America/Matamoros', 'America/Matamoros'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Europe/Rome', 'Europe/Rome'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('America/Lima', 'America/Lima'), ('America/Metlakatla', 'America/Metlakatla'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('US/Michigan', 'US/Michigan'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Europe/Belfast', 'Europe/Belfast'), ('GB-Eire', 'GB-Eire'), ('Pacific/Samoa', 'Pacific/Samoa'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Africa/Dakar', 'Africa/Dakar'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('America/Inuvik', 'America/Inuvik'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/Rosario', 'America/Rosario'), ('America/Marigot', 'America/Marigot'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Regina', 'America/Regina'), ('Europe/Kyiv', 'Europe/Kyiv'), ('US/Alaska', 'US/Alaska'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Europe/Berlin', 'Europe/Berlin'), ('Indian/Cocos', 'Indian/Cocos'), ('Africa/Maseru', 'Africa/Maseru'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Cuba', 'Cuba'), ('Jamaica', 'Jamaica'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Managua', 'America/Managua'), ('America/Curacao', 'America/Curacao'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Brazil/West', 'Brazil/West'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Pacific/Yap', 'Pacific/Yap'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Asia/Macau', 'Asia/Macau'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Menominee', 'America/Menominee'), ('Africa/Harare', 'Africa/Harare'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Etc/GMT+6', 'Etc/GMT+6'), ('US/Eastern', 'US/Eastern'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Belem', 'America/Belem'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Asia/Harbin', 'Asia/Harbin'), ('CST6CDT', 'CST6CDT'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Asia/Anadyr', 'Asia/Anadyr'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('MST7MDT', 'MST7MDT'), ('Africa/Freetown', 'Africa/Freetown'), ('UCT', 'UCT'), ('Europe/Bratislava', 'Europe/Bratislava'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Africa/Conakry', 'Africa/Conakry'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('GB', 'GB'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Australia/Sydney', 'Australia/Sydney'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Iceland', 'Iceland'), ('Europe/Saratov', 'Europe/Saratov'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Kwajalein', 'Kwajalein'), ('Europe/Athens', 'Europe/Athens'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Godthab', 'America/Godthab'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Japan', 'Japan'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Africa/Banjul', 'Africa/Banjul'), ('America/Yakutat', 'America/Yakutat'), ('US/Hawaii', 'US/Hawaii'), ('America/Thule', 'America/Thule'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Asia/Oral', 'Asia/Oral'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Africa/Juba', 'Africa/Juba'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Vienna', 'Europe/Vienna'), ('Africa/Malabo', 'Africa/Malabo'), ('America/Martinique', 'America/Martinique'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Cayman', 'America/Cayman'), ('Asia/Beirut', 'Asia/Beirut'), ('Europe/Moscow', 'Europe/Moscow'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Europe/Prague', 'Europe/Prague'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Africa/Lome', 'Africa/Lome'), ('America/Santarem', 'America/Santarem'), ('Poland', 'Poland'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/Belize', 'America/Belize'), ('Israel', 'Israel'), ('America/Catamarca', 'America/Catamarca'), ('Egypt', 'Egypt'), ('America/Merida', 'America/Merida'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Etc/Universal', 'Etc/Universal'), ('America/Fortaleza', 'America/Fortaleza'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Pacific/Easter', 'Pacific/Easter'), ('Australia/NSW', 'Australia/NSW'), ('Canada/Pacific', 'Canada/Pacific'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/London', 'Europe/London'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('W-SU', 'W-SU'), ('Etc/GMT-12', 'Etc/GMT-12'), ('EST', 'EST'), ('Africa/Kampala', 'Africa/Kampala'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Cordoba', 'America/Cordoba'), ('Europe/Jersey', 'Europe/Jersey'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Moncton', 'America/Moncton'),
                                   ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Vancouver', 'America/Vancouver'), ('America/Tortola', 'America/Tortola'), ('America/Montreal', 'America/Montreal'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('MET', 'MET'), ('Asia/Chungking', 'Asia/Chungking'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Indianapolis', 'America/Indianapolis'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Pacific/Noumea', 'Pacific/Noumea'), ('America/Tijuana', 'America/Tijuana'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Hermosillo', 'America/Hermosillo'), ('Europe/Monaco', 'Europe/Monaco'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('WET', 'WET'), ('Asia/Kabul', 'Asia/Kabul'), ('Eire', 'Eire'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Asia/Yangon', 'Asia/Yangon'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Mexico/General', 'Mexico/General'), ('America/Montevideo', 'America/Montevideo'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Asia/Kuching', 'Asia/Kuching'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Asia/Chita', 'Asia/Chita'), ('America/Shiprock', 'America/Shiprock'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Sitka', 'America/Sitka'), ('Asia/Famagusta', 'Asia/Famagusta'), ('America/Anchorage', 'America/Anchorage'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Hovd', 'Asia/Hovd'), ('Europe/Andorra', 'Europe/Andorra'), ('Australia/Canberra', 'Australia/Canberra'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Boise', 'America/Boise'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Nipigon', 'America/Nipigon'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Brunei', 'Asia/Brunei'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Etc/GMT+2', 'Etc/GMT+2'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Virgin', 'America/Virgin'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Pacific/Palau', 'Pacific/Palau'), ('Asia/Kashgar', 'Asia/Kashgar'), ('UTC', 'UTC'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Singapore', 'Asia/Singapore'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Asia/Aden', 'Asia/Aden'), ('America/Detroit', 'America/Detroit'), ('Europe/Vatican', 'Europe/Vatican'), ('US/Arizona', 'US/Arizona'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Etc/UTC', 'Etc/UTC'), ('America/Maceio', 'America/Maceio'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Libya', 'Libya'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Muscat', 'Asia/Muscat'), ('Navajo', 'Navajo'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Turkey', 'Turkey'), ('GMT0', 'GMT0'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Canada/Mountain', 'Canada/Mountain'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Africa/Lagos', 'Africa/Lagos'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Araguaina', 'America/Araguaina'), ('America/Chihuahua', 'America/Chihuahua'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Canada/Central', 'Canada/Central'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/St_Johns', 'America/St_Johns'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Australia/West', 'Australia/West'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Australia/Hobart', 'Australia/Hobart'), ('Africa/Asmara', 'Africa/Asmara'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Universal', 'Universal'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Indian/Reunion', 'Indian/Reunion'), ('Pacific/Auckland', 'Pacific/Auckland'), ('MST', 'MST'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Tokyo', 'Asia/Tokyo'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('America/Dominica', 'America/Dominica'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Eirunepe', 'America/Eirunepe'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Miquelon', 'America/Miquelon'), ('Iran', 'Iran'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Mazatlan', 'America/Mazatlan'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Etc/GMT+8', 'Etc/GMT+8'), ('America/St_Thomas', 'America/St_Thomas'), ('America/St_Kitts', 'America/St_Kitts'), ('America/New_York', 'America/New_York'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Atikokan', 'America/Atikokan'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Cuiaba', 'America/Cuiaba'), ('Pacific/Efate', 'Pacific/Efate'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Halifax', 'America/Halifax'), ('America/Juneau', 'America/Juneau'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Barbados', 'America/Barbados'), ('HST', 'HST'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('PRC', 'PRC'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Atka', 'America/Atka'), ('America/Rio_Branco', 'America/Rio_Branco'), ('America/Dawson', 'America/Dawson'), ('America/Recife', 'America/Recife'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Guatemala', 'America/Guatemala'), ('Africa/Kigali', 'Africa/Kigali'), ('Africa/Bangui', 'Africa/Bangui'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Europe/Riga', 'Europe/Riga'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Santiago', 'America/Santiago'), ('Etc/GMT', 'Etc/GMT'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('ROK', 'ROK'), ('America/Montserrat', 'America/Montserrat'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Chicago', 'America/Chicago'), ('America/Adak', 'America/Adak'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Aruba', 'America/Aruba'), ('America/Antigua', 'America/Antigua'), ('Pacific/Fiji', 'Pacific/Fiji'), ('EET', 'EET'), ('America/Nuuk', 'America/Nuuk'), ('America/Noronha', 'America/Noronha'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('GMT+0', 'GMT+0'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Europe/Busingen', 'Europe/Busingen'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('America/Mendoza', 'America/Mendoza'), ('Etc/GMT-11', 'Etc/GMT-11'), ('build/etc/localtime', 'build/etc/localtime'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Ojinaga', 'America/Ojinaga'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('US/Pacific', 'US/Pacific'), ('Europe/Malta', 'Europe/Malta'), ('America/Caracas', 'America/Caracas'), ('Asia/Amman', 'Asia/Amman'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Manila', 'Asia/Manila'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Etc/GMT0', 'Etc/GMT0'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Europe/Samara', 'Europe/Samara'), ('Etc/GMT-3', 'Etc/GMT-3'), ('GMT-0', 'GMT-0'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Macao', 'Asia/Macao'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Chile/Continental', 'Chile/Continental'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Africa/Niamey', 'Africa/Niamey'), ('Africa/Tunis', 'Africa/Tunis'), ('Indian/Mahe', 'Indian/Mahe'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Makassar', 'Asia/Makassar'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Asia/Colombo', 'Asia/Colombo'), ('Singapore', 'Singapore'), ('Africa/Cairo', 'Africa/Cairo'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Europe/Kirov', 'Europe/Kirov'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Hongkong', 'Hongkong'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Panama', 'America/Panama'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Europe/Tirane', 'Europe/Tirane'), ('Greenwich', 'Greenwich'), ('Australia/Victoria', 'Australia/Victoria'), ('America/Asuncion', 'America/Asuncion'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Etc/UCT', 'Etc/UCT'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Anguilla', 'America/Anguilla'), ('Africa/Maputo', 'Africa/Maputo'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/Winnipeg', 'America/Winnipeg'), ('Africa/Libreville', 'Africa/Libreville'), ('America/Denver', 'America/Denver'), ('Asia/Damascus', 'Asia/Damascus'), ('Africa/Accra', 'Africa/Accra'), ('America/Guyana', 'America/Guyana'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Etc/GMT+1', 'Etc/GMT+1'), ('GMT', 'GMT'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Europe/Istanbul', 'Europe/Istanbul'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Monterrey', 'America/Monterrey'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Australia/North', 'Australia/North'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/El_Salvador', 'America/El_Salvador'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('America/Creston', 'America/Creston'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Pacific/Midway', 'Pacific/Midway')], default='Europe/London', max_length=35),
        ),
    ]
