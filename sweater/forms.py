from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, PasswordField, SubmitField, SelectField, FieldList, FormField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
from .models import Users, Customer, Technical


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})


def validate_username(self, username):
    existing_user_username = Users.query.filter.by(username=username.data).first()
    if existing_user_username:
        raise ValidationError("That username already exists.Please chose a different one.")


class LoginFrom(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Войти")


class AddClient(FlaskForm):
    name = StringField(validators=[InputRequired()], render_kw={"placeholder": "Имя"})
    surname = StringField(validators=[InputRequired()], render_kw={"placeholder": "Фамилия"})
    debt = StringField(validators=[InputRequired()], render_kw={"placeholder": "Долг в рублях"})
    last_account = StringField(validators=[InputRequired()], render_kw={"placeholder": "Последний счет в рублях"})
    rate = StringField(validators=[InputRequired()], render_kw={"placeholder": "Тариф в рублях"})

    condition_id = SelectField('condition', choices=[], coerce=int)
    status_id = SelectField('status', choices=[], coerce=int)
    payment_method_id = SelectField('payment_method', choices=[], coerce=int)
    payment_type_id = SelectField('payment_type', choices=[], coerce=int)



class UpdateClient(FlaskForm):
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    rate = StringField(validators=[DataRequired()])
    debt = StringField(validators=[DataRequired()])

    condition_id = SelectField('condition', choices=[], coerce=int)
    status_id = SelectField('status', choices=[], coerce=int)
    payment_method_id = SelectField('payment_method', choices=[], coerce=int)
    payment_type_id = SelectField('payment_type', choices=[], coerce=int)

    submit = SubmitField("Обновить клиента")


class AddEquipment(FlaskForm):
    serial_number = StringField(validators=[DataRequired()])
    technical_id = SelectField('technical', choices=[(Technicals.id_technical_list, Technicals.model) for Technicals in
                                        Technical.query.order_by(Technical.model).all()], coerce=int)
    client_id = SelectField('client', choices=[(Customers.id, (Customers.surname, Customers.name)) for Customers in
                                        Customer.query.order_by(Customer.surname).all()], coerce=int)


