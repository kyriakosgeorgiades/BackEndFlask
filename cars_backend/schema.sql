BEGIN TRANSACTION;
DROP TABLE IF EXISTS "car";
CREATE TABLE IF NOT EXISTS "car" (
	"car_id"	,
	"brand" ,
	"model"	,
	"year"	,
	"price" ,
	"km_driven" ,
	"fuel_type" ,
	"seller_type" ,
	"transmission" ,
	"owners_info" ,
	"fuel_consumption" ,
	"engine" ,
	"max_power" ,
	"torque" ,
	"seats" ,
	"image_url" ,
	"user_id"
);
DROP TABLE IF EXISTS "order_info";
CREATE TABLE IF NOT EXISTS "order_info" (
	"order_info_id"	,
	"datetime"	,
	"total"	,
	"user_id"
);
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"user_id" INTEGER PRIMARY KEY,
	"first_name"	,
	"last_name"	,
	"email"	,
	"hash_key" ,
	"hashed_password"	,
	"salt" ,
	"is_admin" BOOLEAN DEFAULT 0
);
DROP TABLE IF EXISTS "car_in_order";
CREATE TABLE IF NOT EXISTS "car_in_order" (
	"order_info_id"	,
	"car_id"
);
DROP TABLE IF EXISTS "basket";
CREATE TABLE IF NOT EXISTS "basket" (
	"user_id"	,
	"car_id"
);
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("1","Ford","Focus","2017","42,995","22,378","Petrol","Individual","Manual","First Owner","59.06","2.3","345","325","5","https://m.atcdn.co.uk/a/media/w800h600/5851b353a37d4541aa3d1c7c50a16848.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("2","Mazda","MX-5","2017","16,999","6,877","Petrol","Dealer","Manual","Second Owner","72.10","1.5","130","112","4","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "order_info" ("order_info_id","datetime","total","user_id") VALUES ('1','2022-01-26 13:45:12','8000','1');
INSERT INTO "user" ("user_id","first_name","last_name","email","hashed_password","salt") VALUES ('1','John','Smith','johnsmith@gmail.com','abc123','321');
INSERT INTO "user" ("user_id","first_name","last_name","email","hashed_password","salt") VALUES ('2','Bob','Marley','bobmarley@gmail.com','abc123','321');
INSERT INTO "car_in_order" ("order_info_id","car_id") VALUES ('1','2');
INSERT INTO "basket" ("user_id","car_id") VALUES ('2','1');
COMMIT;
