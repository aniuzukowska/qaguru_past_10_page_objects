from demoqa_tests.model import app
from demoqa_tests.model.data.user import User


def test_submit_student_details(open_and_quit_browser_automation_practice_form):
    maria = User(
        first_name='Maria',
        last_name='Sklodowska',
        email='maria-sklodowska@gmail.com',
        gender='Female',
        phone_number='1234567890',
        date_of_birth=[7, 'February', '2000'],
        subject='Physics',
        hobby='Music',
        picture='picture.jpg',
        address='France, Paris',
        state='Haryana',
        city='Karnal'
    )

    app.registration_form.register(maria)
    app.registration_form.assert_registered(maria)








