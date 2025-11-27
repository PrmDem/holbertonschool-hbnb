PRAGMA foreign_keys = OFF;

BEGIN TRANSACTION;

CREATE TABLE users (
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(120) NOT NULL,
	password VARCHAR(128) NOT NULL,
	is_admin BOOLEAN,
	id VARCHAR(36) NOT NULL,
	created_at DATETIME,
	updated_at DATETIME,
	PRIMARY KEY (id),
	UNIQUE (email)
);

INSERT INTO
	users
VALUES
	(
		'Admin',
		'HBnB',
		'admin@hbnb.io',
		'$2a$12$hqs4sQBLNsdX0vR69uwjh.1ChJ9YW3hRbd1JFpvDc5xiAlVELcZta',
		1,
		'36c9050e-ddd3-4c3b-9731-9f487208bbc1',
		NULL,
		NULL
	);

INSERT INTO
	users
VALUES
	(
		'Roda',
		'from Dali',
		'innkeep_roda@gaia.io',
		'$2b$12$jMcmHgegHvWf0aiKN497oOePqAo/fsYycCNcgFCjNpNJNyhFfVEXu',
		0,
		'c1889640-851e-4c4f-9d56-c36268b014d8',
		'2025-11-18 14:55:24.197702',
		'2025-11-18 14:55:24.197747'
	);

INSERT INTO
	users
VALUES
	(
		'Kuja',
		'Terrae',
		'pandemonium@terra.io',
		'$2y$10$1VEa/N1E7/wUa8k0XQRVQeWYhdAvMty6ebfA.gPtgJb1SzWX5GKRa',
		0,
		'65a2ebba-95db-4925-8eb8-c883691cab03',
		'2025-11-19 14:19:02',
		'2025-11-19 14:19:02'
	);

INSERT INTO
	users
VALUES
	(
		'Cid',
		'Fabool',
		'cid_faboolix@gaia.io',
		'$2y$10$aq1i55kn6BvpUY8yFY3VU.BO4BgHXsAB01//y7ShJ6ThGTGvVrRYO',
		0,
		'bfd72ffb-bf5f-4aa4-b977-5e59216b023f',
		'2025-11-19 14:19:02',
		'2025-11-19 14:19:02'
	);

INSERT INTO
	users
VALUES
	(
		'Puck',
		'Tallis',
		'hrm_puck@gaia.io',
		'$2y$10$dGDPsGcTXr0.Y5DcNJNyueVzK4EMEgqRB07Uv7kcFY9FpLALuWMw6',
		0,
		'f38ade32-d922-4361-8a3d-53587e7deb1c',
		'2025-11-19 14:21:25',
		'2025-11-19 14:21:25'
	);

INSERT INTO
	users
VALUES
	(
		'N° 234',
		'Mage',
		'blkmage@gaia.io',
		'$2y$10$U8DxcWAPj7QvxyJjcDkS7uSjZot8n0Y/NU3ery8AW.ea9KVBAlor6',
		0,
		'f58122b4-bb59-47b0-a460-c7edf0f2eeb1',
		'2025-11-19 14:28:26',
		'2025-11-19 14:28:26'
	);

INSERT INTO
	users
VALUES
	(
		'Vivi',
		'Ornitia',
		'vivi_lives@gaia.io',
		'$2a$08$ZICtDIRVTT3xhnc3A92FTewTRcOOQFMfMaWXGyWyEZbS/FaIioZGu',
		0,
		'b71fc071-73c7-49c7-b4a5-ca98cb22cbe5',
		'2025-11-19 21:44:52',
		'2025-11-19 21:44:52'
	);

INSERT INTO
	users
VALUES
	(
		'Kildea',
		'Forest Oracle',
		'forest.sings@gaia.io',
		'$2a$10$olK7TAFLAroTeJUWtkcwQ.bH4VIB6zpiee.H6e/4A89JF2g.4USj.',
		0,
		'6d4ded7f-30c2-4b34-ad4e-dbfe4b2f994f',
		'2025-11-22 18:43:27',
		NULL
	);

INSERT INTO
	users
VALUES
	(
		'Garnet',
		'til Alexandros',
		'g.xviith@gaia.io',
		'$2a$10$u3bjsSLRA/d7RISEj99UcOtKlEjpfNhTXVQXXemA8tMCNTYDf662C',
		0,
		'7927496c-da94-42c5-b5d5-fc64617fb560',
		'2025-11-22 18:45:41',
		NULL
	);

INSERT INTO
	users
VALUES
	(
		'Stiltzkin',
		'the Moogle',
		'stiltz@gaia.io',
		'$2a$10$4V3gIhYZzXk2HnurCYSlmujF8M5zV8NvpEUwFTxeottaUzHrOByh6',
		0,
		'c1d9322f-10c0-4002-9971-20f9fd55f357',
		'2025-11-24 13:06:24',
		NULL
	);

CREATE TABLE amenities (
	name VARCHAR(50) NOT NULL,
	id VARCHAR(36) NOT NULL,
	created_at DATETIME,
	updated_at DATETIME,
	PRIMARY KEY (id)
);

INSERT INTO
	amenities
VALUES
	(
		'Washbasin',
		'4f2987a7-c3c5-4a2f-932d-dbc68defe119',
		'2025-11-24 19:24:02',
		NULL
	);

INSERT INTO
	amenities
VALUES
	(
		'Immaterial stairs',
		'f84b3f38-d383-454a-a5fd-caac82920a2b',
		'2025-11-20 09:53:55',
		'2025-11-20 09:53:55'
	);

INSERT INTO
	amenities
VALUES
	(
		'Bunk beds',
		'356fe7ba-0778-44a0-9518-611d5ab92850',
		'2025-11-20 09:54:28',
		'2025-11-20 09:54:28'
	);

INSERT INTO
	amenities
VALUES
	(
		'Book collection',
		'1675d0af-46da-48d0-968b-88f880f25522',
		'2025-11-20 09:55:19',
		'2025-11-20 09:55:19'
	);

INSERT INTO
	amenities
VALUES
	(
		'Colour fortune',
		'57a9b5e9-bb95-45c8-b3af-df7e2c0652d7',
		'2025-11-24 19:22:50',
		'2025-11-24 19:35:45'
	);

INSERT INTO
	amenities
VALUES
	(
		'Prison cells',
		'b47ebca5-64a8-4d8a-9f76-d6531eae469c',
		'2025-11-24 19:22:50',
		NULL
	);

INSERT INTO
	amenities
VALUES
	(
		'Tea table',
		'b116173e-b899-41f0-ac2d-2af867c9c123',
		'2025-11-24 19:29:11',
		NULL
	);

INSERT INTO
	amenities
VALUES
	(
		'Canopy bed',
		'deaddc64-7f44-4654-983b-2e48e41d4ac0',
		'2025-11-24 19:30:28',
		NULL
	);

INSERT INTO
	amenities
VALUES
	(
		'Breakfast',
		'bac4f986-ef49-4dcf-a721-e6435b8a58f4',
		'2025-11-24 19:34:19',
		NULL
	);

INSERT INTO
	amenities
VALUES
	(
		'Gramophone',
		'79a4c314-5e27-4793-922e-278afe1ed785',
		'2025-11-24 19:35:45',
		NULL
	);

INSERT INTO
	amenities
VALUES
	(
		'Airship parking',
		'29ab280f-5abc-4c01-8c78-871ee6d5d1b4',
		'2025-11-24 19:43:54',
		NULL
	);

CREATE TABLE places (
	title VARCHAR(100) NOT NULL,
	description VARCHAR(50),
	price FLOAT NOT NULL,
	latitude FLOAT NOT NULL,
	longitude FLOAT NOT NULL,
	owner_id VARCHAR NOT NULL,
	id VARCHAR(36) NOT NULL,
	created_at DATETIME,
	updated_at DATETIME,
	picture VARCHAR(255),
	location VARCHAR(255),
	PRIMARY KEY (id),
	FOREIGN KEY (owner_id) REFERENCES users (id)
);

INSERT INTO
	places
VALUES
	(
		'Dali Inn',
		'Ideally situated in the quiet village of Dali, this charming one-bedroom inn offers the comforts of home.<br/>With its gorgeous skylight and washbasin, the room itself will help you greet the day with a huge smile on your face. The foyer outside your room will welcome you with a roaring fireplace in winter and refreshing plants in summer.<br/>So what are you waiting for? Discover the peace of rural life today!<p>* Breakfast is a paid option, confirm upon your arrival with the innkeeper',
		100.0,
		25.0,
		30.0,
		'c1889640-851e-4c4f-9d56-c36268b014d8',
		'b36d6b82-2442-4cd2-97a4-85e8b460a9a7',
		'2025-11-18 14:55:38.274807',
		'2025-11-22 18:49:16',
		'images/places/dali',
		'Dali village'
	);

INSERT INTO
	places
VALUES
	(
		'Desert Empress',
		'Protected by numerous quicksands and violent beasts, the Desert Empress is the dream destination for a spiritual or artistic retreat!<br/>As you move around the lava pit, you''ll be moved to tears by the breathtaking artworks: statues, paintings, and the Empress'' signature feature: immaterial stairs.<br/>The ever-dark guest room features an expensive egg-shaped canopy bed, false windows, and every item that didn''t fit the owner''s aesthetic sensibilities.<br/>To compliment the torture chamber, the personal library has a central well to check on the owner''s current hostages – time to make some friends!<p>The Empress: hard to get in, harder to get out!</p>',
		1000.0,
		80.0,
		30.0,
		'65a2ebba-95db-4925-8eb8-c883691cab03',
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'2025-11-19 14:22:44',
		'2025-11-19 14:22:44',
		'images/places/kuja',
		'Kiera Desert'
	);

INSERT INTO
	places
VALUES
	(
		'Pointy Hat inn',
		'Become one of the first to discover the lifestyle of Black Mages! For the first time since its inception, Black Mage village opens its doors to outsiders – and N°234 will be more than happy to welcome you.<br/>Ideally situated between the weapon shop and the water mill, you''ll love waking up to little Bobby''s calls in the morning. And if you hate cute baby chocobos, you can always turn on 234''s gramophone in the main area!<p>Pointy Hat inn: experience true peace.</p>',
		50.0,
		80.0,
		30.0,
		'f58122b4-bb59-47b0-a460-c7edf0f2eeb1',
		'98d5ea1d-d6e8-4f45-9cf8-8dca309becc2',
		'2025-11-19 14:30:19',
		'2025-11-19 14:30:19',
		'images/places/pointy',
		'Black Mage vlg'
	);

INSERT INTO
	places
VALUES
	(
		'Lindblum castle',
		'Lindblum: its heights, its people, its fragrant dried pickles... But have you ever wondered what it looks like from up high?<br/>Through our immersive program, you can now find out for yourself!<br/>What''s it like having a fountain inside the house? What if you needed a lift to go from your bedroom to the living room? Is having a hangar big enough for two airships really all that?<p>Become King Cid''s most honoured guest and find the answer those questions for free*!</p><p><small>(*Inscription fees are required by our service and are not related to the King.)</small></p>',
		5.0,
		35.0,
		30.0,
		'bfd72ffb-bf5f-4aa4-b977-5e59216b023f',
		'bd415e14-d2db-4b29-9619-c4955f68296c',
		'2025-11-19 14:35:51',
		'2025-11-19 14:35:51',
		'images/places/lind',
		'Lindblum'
	);

INSERT INTO
	places
VALUES
	(
		'Cleyra Inn',
		'For a hundred years, Cleyra cut itself off from the rest of the world. Now our favourite rat-people are back, thanks to the late queen Brahne''s war efforts!<br/>Do you need fresh air, pillows stuffed with fluffy feathers, or a challenge for your fear of heights? Look no further!<br/>Since the dismantling of Cleyra''s protective sandstorm, the sky is always blue beyond the evergreen branches of the city-tree. Perfect for sight-seeing and stargazing!<p>Cleyra: the treetop is the limit.</p>',
		150.0,
		45.0,
		30.0,
		'6d4ded7f-30c2-4b34-ad4e-dbfe4b2f994f',
		'14f994a5-9e86-4a9b-98c2-ec74cc29b940',
		'2025-11-22 18:43:49',
		'2025-11-22 18:50:23',
		'images/places/cleyra',
		'Cleyra'
	);

INSERT INTO
	places
VALUES
	(
		'Alexandria Castle',
		'Glamour and romance are in the air with this gorgeous suite in the Royal Castle of Alexandria!<br/>Sleep on the finest mattress, lose consciousness on the most exquisite fainting couch, climb the tower''s spiral staircase until you can''t hold your breakfast down anymore!<br/>Everything is possible when you walk in queen Garnet''s kitten-heeled footsteps.<p>By becoming a patron, you will fund the glorious new era of Alexandria. Rebuild, restore, reconnect.</p>',
		300.0,
		25.0,
		30.0,
		'7927496c-da94-42c5-b5d5-fc64617fb560',
		'1010e46e-934f-434b-abfb-c320c2bd3d17',
		'2025-11-22 18:47:54',
		NULL,
		'images/places/alex',
		'Alexandria'
	);

CREATE TABLE place_amenity (
	place_id VARCHAR NOT NULL,
	amenity_id VARCHAR NOT NULL,
	PRIMARY KEY (place_id, amenity_id),
	FOREIGN KEY (place_id) REFERENCES places (id),
	FOREIGN KEY (amenity_id) REFERENCES amenities (id)
);

INSERT INTO
	place_amenity
VALUES
	(
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'f84b3f38-d383-454a-a5fd-caac82920a2b'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'1675d0af-46da-48d0-968b-88f880f25522'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'b36d6b82-2442-4cd2-97a4-85e8b460a9a7',
		'1675d0af-46da-48d0-968b-88f880f25522'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'b36d6b82-2442-4cd2-97a4-85e8b460a9a7',
		'4f2987a7-c3c5-4a2f-932d-dbc68defe119'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'b36d6b82-2442-4cd2-97a4-85e8b460a9a7',
		'57a9b5e9-bb95-45c8-b3af-df7e2c0652d7'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'b47ebca5-64a8-4d8a-9f76-d6531eae469c'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'deaddc64-7f44-4654-983b-2e48e41d4ac0'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'98d5ea1d-d6e8-4f45-9cf8-8dca309becc2',
		'79a4c314-5e27-4793-922e-278afe1ed785'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'98d5ea1d-d6e8-4f45-9cf8-8dca309becc2',
		'356fe7ba-0778-44a0-9518-611d5ab92850'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'bd415e14-d2db-4b29-9619-c4955f68296c',
		'b116173e-b899-41f0-ac2d-2af867c9c123'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'bd415e14-d2db-4b29-9619-c4955f68296c',
		'bac4f986-ef49-4dcf-a721-e6435b8a58f4'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'14f994a5-9e86-4a9b-98c2-ec74cc29b940',
		'bac4f986-ef49-4dcf-a721-e6435b8a58f4'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'14f994a5-9e86-4a9b-98c2-ec74cc29b940',
		'1675d0af-46da-48d0-968b-88f880f25522'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'1010e46e-934f-434b-abfb-c320c2bd3d17',
		'b116173e-b899-41f0-ac2d-2af867c9c123'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'1010e46e-934f-434b-abfb-c320c2bd3d17',
		'deaddc64-7f44-4654-983b-2e48e41d4ac0'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'1010e46e-934f-434b-abfb-c320c2bd3d17',
		'bac4f986-ef49-4dcf-a721-e6435b8a58f4'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'1010e46e-934f-434b-abfb-c320c2bd3d17',
		'b47ebca5-64a8-4d8a-9f76-d6531eae469c'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'29ab280f-5abc-4c01-8c78-871ee6d5d1b4'
	);

INSERT INTO
	place_amenity
VALUES
	(
		'bd415e14-d2db-4b29-9619-c4955f68296c',
		'29ab280f-5abc-4c01-8c78-871ee6d5d1b4'
	);

CREATE TABLE reviews (
	text VARCHAR NOT NULL,
	rating INTEGER NOT NULL,
	place_id VARCHAR(60) NOT NULL,
	user_id VARCHAR(60) NOT NULL,
	id VARCHAR(36) NOT NULL,
	created_at DATETIME,
	updated_at DATETIME,
	PRIMARY KEY (id),
	FOREIGN KEY (place_id) REFERENCES places (id),
	FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO
	reviews
VALUES
	(
		'It was my first time seeing windmills! <br/>Also, I got kidnapped.',
		4,
		'b36d6b82-2442-4cd2-97a4-85e8b460a9a7',
		'b71fc071-73c7-49c7-b4a5-ca98cb22cbe5',
		'b9569c99-09bd-4d7a-854f-39718262aab5',
		'2025-11-20 13:05:07',
		'2025-11-23 22:34:17'
	);

INSERT INTO
	reviews
VALUES
	(
		'The immaterial stairs were very pretty but very hard to use. Also, I got kidnapped.',
		3,
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'b71fc071-73c7-49c7-b4a5-ca98cb22cbe5',
		'ec3fa2b2-26d5-4bdb-a590-05be9af3c9e3',
		'2025-11-22 16:56:53.965210',
		'2025-11-22 16:56:53.965221'
	);

INSERT INTO
	reviews
VALUES
	(
		'It was SOOOOO cool there!!! I got to see my pal Vivi again, also Freyja teh badass dragon knight lady, AND I almost got eaten by an antlion!!! My dad was there but he didn''t bother me too much since he was busy doing war stuff. 5 outta 5!!!',
		5,
		'14f994a5-9e86-4a9b-98c2-ec74cc29b940',
		'f38ade32-d922-4361-8a3d-53587e7deb1c',
		'60fa68bd-1e28-4246-855c-1b51058a7de1',
		'2025-11-22 20:02:50.462426',
		'2025-11-22 20:02:50.462440'
	);

INSERT INTO
	reviews
VALUES
	(
		'I can''t deny the Empress''s beauty, but the room my wife was held hostage in for years didn''t have any windows! Can you believe!? With all the glass-stained work around the place!?<br/>Anyway, I hope the owner got rid of the Hedgehog Pie that''s in the torture chamber. I didn''t like that little beast one bit!',
		2,
		'dca93149-2531-429e-8763-9b8c2d57bce3',
		'bfd72ffb-bf5f-4aa4-b977-5e59216b023f',
		'4c49aec0-2fd8-4813-b0b5-292bafc3cd44',
		'2025-11-24 13:49:46.064772',
		'2025-11-24 13:49:46.064792'
	);

INSERT INTO
	reviews
VALUES
	(
		'I''ll never forget my stay there. I will miss everyone, but I''ll definitely come back someday.',
		5,
		'98d5ea1d-d6e8-4f45-9cf8-8dca309becc2',
		'b71fc071-73c7-49c7-b4a5-ca98cb22cbe5',
		'181737ab-de7e-409c-a8df-8f94938bfa0d',
		'2025-11-24 13:58:00.382856',
		'2025-11-24 13:58:00.382865'
	);

INSERT INTO
	reviews
VALUES
	(
		'Business wasn''t very good, but always better than in Burmecia. I almost got swept away by the sandstorm!',
		4,
		'14f994a5-9e86-4a9b-98c2-ec74cc29b940',
		'c1d9322f-10c0-4002-9971-20f9fd55f357',
		'f37ae56e-96bc-46ce-a529-a61a8db1744e',
		'2025-11-24 14:08:55.805155',
		'2025-11-24 14:08:55.805163'
	);

ANALYZE sqlite_schema;

INSERT INTO
	sqlite_stat1
VALUES
	('reviews', 'sqlite_autoindex_reviews_1', '3 1');

INSERT INTO
	sqlite_stat1
VALUES
	(
		'place_amenity',
		'sqlite_autoindex_place_amenity_1',
		'3 2 1'
	);

INSERT INTO
	sqlite_stat1
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'6 1'
	);

INSERT INTO
	sqlite_stat1
VALUES
	('users', 'sqlite_autoindex_users_2', '9 1');

INSERT INTO
	sqlite_stat1
VALUES
	('users', 'sqlite_autoindex_users_1', '9 1');

INSERT INTO
	sqlite_stat1
VALUES
	('places', 'sqlite_autoindex_places_1', '6 1');

ANALYZE sqlite_schema;

INSERT INTO
	sqlite_stat4
VALUES
	(
		'reviews',
		'sqlite_autoindex_reviews_1',
		'1 1',
		'0 0',
		'0 0',
		X'03550136306661363862642d316532382d343234362d383535632d31623531303538613764653103'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'reviews',
		'sqlite_autoindex_reviews_1',
		'1 1',
		'1 1',
		'1 1',
		X'03550962393536396339392d303962642d346437612d383534662d333937313832363261616235'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'reviews',
		'sqlite_autoindex_reviews_1',
		'1 1',
		'2 2',
		'2 2',
		X'03550165633366613262322d323664352d346264622d613539302d30356265396166336339653302'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'place_amenity',
		'sqlite_autoindex_place_amenity_1',
		'1 1 1',
		'0 0 0',
		'0 0 0',
		X'0455550162333664366238322d323434322d346364322d393761342d38356538623436306139613731363735643061662d343664612d343864302d393638622d38386638383066323535323203'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'place_amenity',
		'sqlite_autoindex_place_amenity_1',
		'2 1 1',
		'1 1 1',
		'1 1 1',
		X'0455550164636139333134392d323533312d343239652d383736332d39623863326435376263653331363735643061662d343664612d343864302d393638622d38386638383066323535323202'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'place_amenity',
		'sqlite_autoindex_place_amenity_1',
		'2 1 1',
		'1 2 2',
		'1 2 2',
		X'0455550964636139333134392d323533312d343239652d383736332d39623863326435376263653366383462336633382d643338332d343534612d613566642d636161633832393230613262'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'1 1',
		'0 0',
		'0 0',
		X'03550131363735643061662d343664612d343864302d393638622d38386638383066323535323206'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'1 1',
		'1 1',
		'1 1',
		X'03550931646534306638372d346330312d343763652d613738382d363536326630366633326434'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'1 1',
		'2 2',
		'2 2',
		X'03550133353666653762612d303737382d343461302d393531382d36313164356162393238353005'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'1 1',
		'3 3',
		'3 3',
		X'03550134663239383761372d633363352d346132662d393332642d64626336386465666531313902'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'1 1',
		'4 4',
		'4 4',
		X'03550136613938616366392d613465392d343637332d623061372d63666531313037613962316203'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'amenities',
		'sqlite_autoindex_amenities_1',
		'1 1',
		'5 5',
		'5 5',
		X'03550166383462336633382d643338332d343534612d613566642d63616163383239323061326204'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'0 0',
		'0 0',
		X'03270961646d696e4068626e622e696f'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'1 1',
		'1 1',
		X'032b01626c6b6d61676540676169612e696f07'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'2 2',
		'2 2',
		X'0335016369645f6661626f6f6c697840676169612e696f05'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'3 3',
		'3 3',
		X'033501666f726573742e73696e677340676169612e696f09'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'4 4',
		'4 4',
		X'032d01672e78766969746840676169612e696f0a'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'5 5',
		'5 5',
		X'032d0168726d5f7075636b40676169612e696f06'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'6 6',
		'6 6',
		X'033501696e6e6b6565705f726f646140676169612e696f03'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'7 7',
		'7 7',
		X'03350170616e64656d6f6e69756d4074657272612e696f04'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_2',
		'1 1',
		'8 8',
		'8 8',
		X'033101766976695f6c6976657340676169612e696f08'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'0 0',
		'0 0',
		X'03550933366339303530652d646464332d346333622d393733312d396634383732303862626331'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'1 1',
		'1 1',
		X'03550136356132656262612d393564622d343932352d386562382d63383833363931636162303304'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'2 2',
		'2 2',
		X'03550136643464656437662d333063322d346233342d616434652d64626665346232663939346609'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'3 3',
		'3 3',
		X'03550137393237343936632d646139342d343263352d623564352d6663363436313766623536300a'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'4 4',
		'4 4',
		X'03550162373166633037312d373363372d343963372d623461352d63613938636232326362653508'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'5 5',
		'5 5',
		X'03550162666437326666622d626635662d346161342d623937372d35653539323136623032336605'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'6 6',
		'6 6',
		X'03550163313838393634302d383531652d346334662d396435362d63333632363862303134643803'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'7 7',
		'7 7',
		X'03550166333861646533322d643932322d343336312d386133642d35333538376537646562316306'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'users',
		'sqlite_autoindex_users_1',
		'1 1',
		'8 8',
		'8 8',
		X'03550166353831323262342d626235392d343762302d613436302d63376564663066326565623107'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'places',
		'sqlite_autoindex_places_1',
		'1 1',
		'0 0',
		'0 0',
		X'03550131303130653436652d393334662d343334622d616266622d63333230633262643364313706'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'places',
		'sqlite_autoindex_places_1',
		'1 1',
		'1 1',
		'1 1',
		X'03550131346639393461352d396538362d346139622d393863322d65633734636332396239343005'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'places',
		'sqlite_autoindex_places_1',
		'1 1',
		'2 2',
		'2 2',
		X'03550139386435656131642d643665382d346634352d396366382d38646361333039626563633203'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'places',
		'sqlite_autoindex_places_1',
		'1 1',
		'3 3',
		'3 3',
		X'03550962333664366238322d323434322d346364322d393761342d383565386234363061396137'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'places',
		'sqlite_autoindex_places_1',
		'1 1',
		'4 4',
		'4 4',
		X'03550162643431356531342d643264622d346232392d393631392d63343935356636383239366304'
	);

INSERT INTO
	sqlite_stat4
VALUES
	(
		'places',
		'sqlite_autoindex_places_1',
		'1 1',
		'5 5',
		'5 5',
		X'03550164636139333134392d323533312d343239652d383736332d39623863326435376263653302'
	);

COMMIT;