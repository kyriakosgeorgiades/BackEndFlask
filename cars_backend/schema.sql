BEGIN TRANSACTION;
DROP TABLE IF EXISTS "car";
CREATE TABLE IF NOT EXISTS "car" (
	"car_id"	,
	"model"	,
	"year"	,
	"colour"	,
	"price"	,
	"number_of_doors"	,
	"number_of_seats"	,
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
INSERT INTO "car" ("car_id","model","year","colour","price","number_of_doors","number_of_seats","user_id") VALUES ('1','Audi G8','2018','Dark Blue','26000','4','5','1');
INSERT INTO "car" ("car_id","model","year","colour","price","number_of_doors","number_of_seats","user_id") VALUES ('2','BMW F27','2006','White','8000','2','4','2');
INSERT INTO "order_info" ("order_info_id","datetime","total","user_id") VALUES ('1','2022-01-26 13:45:12','8000','1');
INSERT INTO "user" ("user_id","first_name","last_name","email","hashed_password","salt") VALUES ('1','John','Smith','johnsmith@gmail.com','abc123','321');
INSERT INTO "user" ("user_id","first_name","last_name","email","hashed_password","salt") VALUES ('2','Bob','Marley','bobmarley@gmail.com','abc123','321');
INSERT INTO "car_in_order" ("order_info_id","car_id") VALUES ('1','2');
INSERT INTO "basket" ("user_id","car_id") VALUES ('2','1');
COMMIT;
