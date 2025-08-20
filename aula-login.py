@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    db = SessionLocalExemplo()

    try:
        sql = select(UsuarioExemplo).where(UsuarioExemplo.email == email)
        user = db.execute(sql).scalar()

        if user and user.check_password(senha):
            print("if login")
            access_token = create_access_token(identity=str(user.email))
            return jsonify({
                "access_token":access_token,
                "papel": user.papel,
            }), 200
        return jsonify({"msg": "Credenciais inválidas"}), 401
    except Exception as e:
        print(e)
        return jsonify({"msg": str(e)}), 500
    finally:
        db.close()