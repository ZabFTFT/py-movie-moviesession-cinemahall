from django.db.models import QuerySet, F

from db.models import MovieSession


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> None:
    movie_session_to_update = MovieSession.objects.filter(id=session_id)

    movie_session_to_update.update(
        show_time=F("show_time") if not show_time else show_time,
        cinema_hall_id=F("cinema_hall_id")
        if not cinema_hall_id
        else cinema_hall_id,
        movie_id=F("movie_id") if not movie_id else movie_id,
    )


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
