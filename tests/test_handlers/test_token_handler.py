import json

def test_get_token(client):
    request_data = {
        'login': 'VasiliyLogin',
        'password': 'PasswordVasiliya',
    }
    resp = client.post(f'/get_token', data=json.dumps(request_data))
    data_from_resp = resp.json()
    assert resp.status_code == 200
    assert data_from_resp['token'] == request_data['login']