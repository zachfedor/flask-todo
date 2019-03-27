from flask import Flask, flash, make_response, render_template, request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/')
    def index():
        # TODO: Get todos from database
        mock_todos = [
            { "text": "do dishes", "created_at": "2019-03-22", "completed": False },
            { "text": "feed dog", "created_at": "2019-03-22", "completed": False },
            { "text": "clean room", "created_at": "2019-03-22", "completed": True },
        ]

        filter_option = request.args.get('filter')
        if filter_option == 'completed':
            mock_todos = list(filter(lambda t: t['completed'], mock_todos))
        elif filter_option == 'active':
            mock_todos = list(filter(lambda t: not t['completed'], mock_todos))

        # TODO: add ability to sort items
        # sort_option = request.args.get('sort')

        return render_template('index.html', todos=mock_todos, filter_option=filter_option)


    @app.route('/create', methods=["GET", "POST"])
    def create():
        if request.method == "POST":
            # TODO: Save request.form data to database
            # TODO: If error, flash it to the screen
            new_item = request.form["text"]

            if new_item:
                print("Create Todo: ", new_item)
                flash('To-Do item was added. Want to add another?', 'success')
            else:
                flash('You need to add some text first.', 'error')


        return render_template('create.html')


    return app

