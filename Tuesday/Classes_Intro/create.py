from app import db, Countries

db.drop_all()
db.create_all()


testplace = Countries(id='Spain', continent='Europe', climate='hot and dry')
db.session.add(testplace)
db.session.commit()