# BLUEPRINT | DONT EDIT
import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

def getMovie(url, movie_id):
    try:
        response = requests.get(f"{url}/movies/{movie_id}", timeout=10)
        # response.raise_for_status()  # HTTP 상태 코드 확인, 커스텀 상태 코드 메시지 출력한다고 하면 이부분 제외하면 된다.

    except requests.exceptions.Timeout:
        print(f"Request timed out for movie ID {movie_id}")
        return
    except requests.exceptions.ConnectionError:
        print(f"Connection error for movie ID {movie_id}")
        return
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error for movie ID {movie_id}: {http_err}")
        return
    except requests.exceptions.RequestException as req_err:
        print(f"Request failed for movie ID {movie_id}: {req_err}")
        return
    
    # 커스텀 상태 코드 메시지
    if 500 <= response.status_code < 600:
        print("Server Error")
        return
    elif 400 <= response.status_code < 500:
        print("Client Error")
        return
    elif 300 <= response.status_code < 400:
        print("Redirection Messages")
        return

    try:
        data = response.json()
    except ValueError: # ValueError는 주로 값 자체가 적합하지 않을 때 처리한다. ex) JSON 파싱 실패, 함수 호출 시 잘못된 타입이나 범위의 값을 전달했을 때 경우.
        print("Invalid JSON response")
        return
    return data

    

url = "https://nomad-movies.nomadcoders.workers.dev"

for movie_id in movie_ids:
    movie = getMovie(url, movie_id)

    if movie:
        print(f"Movie ID: {movie_id}")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Vote Average: {round(movie['vote_average'], 2)}")
        print("=====================================")
    else:
        print(f"No movie data for Movie ID {movie_id}")
        print("=====================================")

# /YOUR CODE