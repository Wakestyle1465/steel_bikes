from models import Bike, db
from app import app


db.drop_all()
db.create_all()

jumper = Bike(name='Steel Jumper', price = '2349.99', color = 'Deep Blue', description = 'The Stumpjumper Alloy brings all-new suspension kinematics and progressive geometry into a full-alloy package thats both lightweight and extremely durable. Outfitted with a no-fuss SRAM SX 12-speed groupset, the Stumpjumper Alloy is your all-access pass for trail adventure.', size = 29, image_url = 'https://cdn.shopify.com/s/files/1/2318/5263/products/BMT23309_PH2_01_850x850.jpg?v=1644001548')
fusion = Bike(name='Steel Fusion', price = '1439.00', color = 'Black', size = 29, description = 'The Fusion is the perfect blend of efficiency, capability, and reliability on the trail. The Fusion’s responsive handling characteristics and comfortable geometry will help you mix up your ride from the pathway, to the trail, and onto the singletrack.', image_url='https://cdn.shopify.com/s/files/1/2318/5263/products/BMT19294__PH_1_336x336.jpg?v=1656530416')
cycles = Bike(name='Steel Cycles', price = '7499.99', color = 'Powder Blue', size = 29, description = 'If you follow the EWS, the SB150 doesnt need an intro. This is the winningest race bike in EWS history. Its more capable than the 140, and has more modern geo and features than the SB6, like wider shock compatibility and updated kinematics.',image_url = 'https://cdn.shopify.com/s/files/1/2318/5263/products/BMT26493_PH_1_336x336.jpg?v=1658507369')
epic = Bike(name='Steel Epic Pro', price = '8499.99', color = 'White', size = 29, description = 'Simply put, the Epic is a cross country weapon. Being lightweight and fast is what this bike is all about. The BRAIN shock delivers crazy traction and makes this full-suspension feel as fast as a hardtail. This efficient partner will save your legs on long trail rides or XC races with ample climbs and tight, techy terrain.', image_url = 'https://cdn.shopify.com/s/files/1/2318/5263/products/BMT26997_PH_1_336x336.jpg?v=1658514055')
procal = Bike(name='Steel ProCal', price = '2499.99', color = 'Red', size = 29, description = 'The Procaliber is a proven World Cup contender. It’s lighter and more agile than the Supercaliber, but still extremely capable over the rough stuff. With lightweight OCLV mountain carbon, the frame is smooth and stiff - aided by the rear IsoSpeed decoupler. Whether you’re at the race loop or sweeping local singletrack, it won’t let you down.', image_url ='https://cdn.shopify.com/s/files/1/2318/5263/products/BMT26658_PH_1_336x336.jpg?v=1658509801')

db.session.add_all([jumper,fusion,cycles,epic,procal])
db.session.commit()