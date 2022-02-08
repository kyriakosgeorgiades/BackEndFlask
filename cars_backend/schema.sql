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
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("3","MINI","Cooper Roadster Convertible","2012","9,000","44,540","Petrol","Dealer","Manual","Second Owner","42.80","1.6","190","192","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("4","MINI","Cooper Roadster Convertible","2012","8,483","68,897","Petrol","Individual","Manual","Second Owner","42.80","1.6","190","192","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("5","AM","General Hummer","2000","68,999","87,972","Diesel","Dealer","Manual","Second Owner","19.50","3.7","244","241","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("6","AM","General Hummer","2000","53,029","103,873","Diesel","Individual","Manual","Second Owner","19.50","3.7","244","241","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("7","BMW","Z4 Convertible","2012","12,978","74,407","Petrol","Dealer","Automatic","Second Owner","41.50","2.0","245","258","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("8","BMW","Z4 Convertible","2012","14,999","83,287","Petrol","Individual","Automatic","Second Owner","41.50","2.0","245","258","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("9","Bugatti","Veyron Convertible","2009","1,902,999","124","Petrol","Dealer","Manual","Second Owner","8.00","8.0","1001","922","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("10","Bugatti","Veyron Convertible","2009","1,093,042","8,009","Petrol","Individual","Manual","Second Owner","8.00","8.0","1001","922","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("11","Bugatti","Veyron Coupe","2009","983,847","32,092","Petrol","Dealer","Manual","Second Owner","8.00","8.0","1001","922","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("12","Bugatti","Veyron Coupe","2009","864,957","50,198","Petrol","Individual","Manual","Second Owner","8.00","8.0","1001","922","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("13","Geo","Metro Convertible","1993","500","126,877","Petrol","Dealer","Manual","Second Owner","2.00","1.1","59","66","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("14","Geo","Metro Convertible","1993","999","98,020","Petrol","Individual","Manual","Second Owner","2.00","1.1","59","66","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("15","Jaguar","XK XKR","2012","35,997","16,877","Petrol","Dealer","Manual","Second Owner","18.00","5.0","385","380","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("16","Jaguar","XK XKR","2012","38,329","26,457","Petrol","Dealer","Manual","Second Owner","18.00","5.0","385","380","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("17","Jeep","Liberty","2012","16,000","46,877","Diesel","Dealer","Manual","Second Owner","14.00","3.7","210","199","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("18","Jeep","Liberty","2012","19,999","26,567","Diesel","Individual","Manual","Second Owner","14.00","3.7","210","199","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("19","Mercedes-Benz","300-Class","1993","6,999","97,801","Petrol","Dealer","Automatic","Second Owner","23.00","3.2","217","201","7","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("20","Mercedes-Benz","300-Class","1993","1,034","146,877","Petrol","Dealer","Automatic","Second Owner","23.00","3.2","217","201","7","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("21","Mercedes-Benz","Sprinter","2012","36,999","34,007","Diesel","Individual","Manual","Second Owner","35.30","2.1","141","243","7","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("22","Mercedes-Benz","Sprinter","2012","42,482","26,877","Diesel","Dealer","Manual","Second Owner","35.30","2.1","141","243","7","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("23","Mitsubishi","Lancer Sedan","2012","76,182","3,137","Petrol","Dealer","Manual","Second Owner","8.10","2.0","148","140","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("24","Mitsubishi","Lancer Sedan","2012","96,929","1,877","Petrol","Individual","Manual","Second Owner","8.10","2.0","148","140","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("25","Tesla","Model S Sedan","2012","99,999","1,001","Electric","Dealer","Automatic","Second Owner","265.0","1.0","356","400","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("26","Tesla","Model S Sedan","2012","116,999","234","Electric","Dealer","Automatic","Second Owner","265.0","1.0","356","400","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("27","Scion","xD Hatchback","2012","929","201,001","Petrol","Individual","Manual","Second Owner","27.30","1.8","128","125","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("28","Scion","xD Hatchback","2012","219","999,999","Petrol","Dealer","Manual","Second Owner","27.30","1.8","128","125","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("29","Aston Martin","Virage Coupe","2012","116,999","877","Petrol","Dealer","Manual","Second Owner","15.60","8.0","489","501","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("30","Aston Martin","Virage Coupe","2012","161,000","6","Petrol","Dealer","Manual","Second Owner","15.60","8.0","489","501","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("31","Rolls-Royce","Phantom Sedan","2012","162,999","7","Petrol","Individual","Automatic","Second Owner","12.01","6.8","453","531","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("32","Rolls-Royce","Phantom Sedan","2012","216,999","1","Petrol","Dealer","Automatic","Second Owner","12.01","6.8","453","531","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("33","Spyker","C8 Coupe","2009","87,000","23,877","Petrol","Dealer","Manual","Second Owner","23.20","4.0","620","637","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("34","Spyker","C8 Coupe","2009","92,999","21,877","Petrol","Individual","Manual","Second Owner","23.20","4.0","620","637","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("35","Suzuki","SX4 Hatchback","2012","6,999","83,877","Petrol","Dealer","Manual","Second Owner","45.60","1.6","118","115","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("36","Suzuki","SX4 Hatchback","2012","8,000","63,877","Petrol","Dealer","Manual","Second Owner","45.60","1.6","118","115","5","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("37","Bentley","Continental GT Coupe","2012","64,983","72,877","Petrol","Dealer","Manual","Second Owner","7.35","6.0","507","545","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type","transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url","user_id") VALUES ("38","Bentley","Continental GT Coupe","2012","103,487","2,817","Petrol","Dealer","Manual","Second Owner","7.35","6.0","507","545","2","https://m.atcdn.co.uk/a/media/w1024/585eef6dbaf44c719ab4c5524fb45fb7.jpg","1");
INSERT INTO "order_info" ("order_info_id","datetime","total","user_id") VALUES ('1','2022-01-26 13:45:12','8000','1');
INSERT INTO "user" ("user_id","first_name","last_name","email","hashed_password","salt") VALUES ('1','John','Smith','johnsmith@gmail.com','abc123','321');
INSERT INTO "user" ("user_id","first_name","last_name","email","hashed_password","salt") VALUES ('2','Bob','Marley','bobmarley@gmail.com','abc123','321');
INSERT INTO "car_in_order" ("order_info_id","car_id") VALUES ('1','2');
INSERT INTO "basket" ("user_id","car_id") VALUES ('2','1');
COMMIT;
