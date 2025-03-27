from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Thomaz', email='test@gmail.com', password='senhafoda'
    )

    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'test@gmail.com'))

    assert result.username == 'Thomaz'
