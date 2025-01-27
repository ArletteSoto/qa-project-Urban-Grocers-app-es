import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

# Función de prueba positiva
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función de prueba negativa
def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

# Prueba 1. Kit creada con éxito. El parámetro name contiene 1 caracter
def test1_create_kit_1_letter_in_name_get_success_response():
    current_kit_body = get_kit_body("a")
    positive_assert(current_kit_body)

# Prueba 2. Kit creada con éxito. El parámetro name contiene 511 caracteres
def test2_create_kit_511_letter_in_name_get_success_response():
    current_kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                                    "cdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcd"\
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                                    "cdabC")
    positive_assert(current_kit_body)

# Prueba 3. Error. El número de caracteres es menor que la cantidad permitida (0)
def test3_create_kit_0_letter_in_name_get_error_response():
    current_kit_body = get_kit_body("")
    negative_assert_400(current_kit_body)

# Prueba 4. Error. El número de caracteres es mayor que la cantidad permitida (512)
def test4_create_kit_512_letter_in_name_get_error_response():
    negative_assert_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                        "abcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdab"\
                        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Kit creada con éxito. El parámetro name permite caracteres especiales
def test5_create_kit_has_special_symbol_in_name_get_success_response():
    current_kit_body = get_kit_body("№%@,")
    positive_assert(current_kit_body)


# Prueba 6. Kit creada con éxito. El parámetro name permite espacios
def test6_create_kit_has_spaces_in_name_get_succes_response():
    current_kit_body = get_kit_body("A Aaa")
    positive_assert(current_kit_body)

# Prueba 7. Kit creada con éxito. Se permiten números
def test7_create_kit_has_numbers_in_name_get_succes_response():
    current_kit_body = get_kit_body("123")
    positive_assert(current_kit_body)


# Prueba 8. Error. El parámetro no se pasa en la solicitud
def test8_create_kit_without_name_parameter_get_error_response():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)


# Prueba 9. Error. Se ha pasado un tipo de parámetro diferente (número)
def test9_create_kit_number_type_first_name_get_error_response():
    current_kit_body = get_kit_body(123)
    negative_assert_400(current_kit_body)