

valid_input = True
while valid_input:
    result_id = input('=>')
    try:
        if tournament_table.get(doc_id=int(result_id)) is not None:
            valid_input = False
        else:
            print('le nombre indiquer ne mene a rien')
            valid_input = True
    except ValueError:
        print("merci d'entré un nombre")