from app.app_controller import app, create_tables, add_user, get_tables, drop_table

if __name__ == "__main__":
    with app.app_context():
        create_tables()
        #add_user('Ardian', 440)
        print( f'Table names before drop: { get_tables() }')
        #drop_table('notes')
        #drop_table('users')
        print( f'Table names after drop: { get_tables() }')
    app.run(host="127.0.0.1", port=5000)   # , ssl_context=('crt.pem', 'key.pem')