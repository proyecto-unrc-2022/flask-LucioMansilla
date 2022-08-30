from behave import fixture, use_fixture
from application import app

@fixture
def application_client(context, *args, **kwargs):
    # app.testing = True
    app.config.update({
        "TESTING": True,
    })

    context.client = app.test_client()
    
    yield context.client

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(application_client, context)

@fixture()
def runner(app):
    return app.test_cli_runner()
