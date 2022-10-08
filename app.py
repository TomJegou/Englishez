
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Infinitif = db.Column(db.String(200), nullable=False)
    Preterit = db.Column(db.String(200), nullable=False)
    Participe = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<{self.Infinitif} {self.Preterit} {self.Participe}>'


@app.route('/reviser', methods=['POST', 'GET'])
def reviser():
    verbes = Todo.query.all()
    return render_template('reviser.html', verbes=verbes)


@app.route('/entrainement', methods=['POST', 'GET'])
def entrainement():
    temps = random.choice(['Participe', 'Preterit'])
    if request.method == 'POST':
        reponse = request.form['reponse']
        verbe_infi = request.form['verbe']
        temps_verbe = request.form['temps_verbe']
        verbe = Todo.query.filter_by(Infinitif=verbe_infi).first()
        if temps_verbe == 'Participe':
            if reponse == verbe.Participe:
                return render_template('bonnerep.html')
            else:
                return render_template('mauvaiserep.html')
        else:
            if reponse == verbe.Preterit:
                return render_template('bonnerep.html')
            else:
                return render_template('mauvaiserep.html')
    else:
        verbes = Todo.query.all()
        id = random.randint(0, len(verbes))
        verbe = verbes[id]
        if temps == 'Participe':
            c = verbe.Participe
        else:
            c = verbe.Preterit
        print(verbe)
        return render_template('entrainement.html', verbe=verbe, temps=temps, c=c)


@app.route('/entrainement2', methods=['POST', 'GET'])
def entrainement2():
    temps = random.choice(['Participe', 'Preterit'])
    if request.method == 'POST':
        reponse = request.form['reponse']
        verbe_infi = request.form['verbe']
        temps_verbe = request.form['temps_verbe']
        verbe = Todo.query.filter_by(Infinitif=verbe_infi).first()

        if temps_verbe == 'Participe':
            if reponse == verbe.Participe:
                return render_template('bonnerep.html')
            else:
                return render_template('mauvaiserep.html')

        else:
            if reponse == verbe.Preterit:
                return render_template('bonnerep.html')
            else:
                return render_template('mauvaiserep.html')

    else:
        verbes = Todo.query.all()
        id = random.randint(0, len(verbes))
        verbe = verbes[id]
        print(verbe)
        if temps == 'Participe':
            return render_template('entrainement2ex1.html', verbe=verbe, temps=temps)
        else:
            return render_template('entrainement2ex2.html', verbe=verbe,temps=temps)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    """   verbe = Todo(Infinitif = 'be', Preterit = 'was', Participe = 'been')
    db.session.add(verbe)
    db.session.commit()
    verbe = Todo.query.filter_by(id=VerbeId).first() 
    ou Todo.query.filter_by(Infinitif=VerbeInfinitif).first()
    print(verbe.infinitif)

    # deleted

    db.session.delete(verbe)
    db.session.commit()


    lignes = []
    colonnes = []
    d = []
    v = []
    with open('Verbes irréguliers.txt', 'r') as verbes_txt:
        for ligne in verbes_txt.readlines():
            for lettre in ligne:
                if lettre == '\n':
                    v.append(''.join(d))
                    colonnes.append(v)
                    v = []
                    d = []

                elif lettre == '\t':
                    v.append(''.join(d))
                    colonnes.append(v)
                    v = []
                    d = []
                else:
                    d.append(lettre)

            lignes.append(colonnes)
            colonnes = []
    del lignes[134]
    for i in range(1,len(lignes)-1):
        verbe = Todo(Infinitif=lignes[i][0][0], Preterit=lignes[i][1][0], Participe=lignes[i][2][0])
        db.session.add(verbe)
        db.session.commit()
    db.create_all()
    """
    app.run(debug=True)

