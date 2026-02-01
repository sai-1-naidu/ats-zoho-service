applications = []

def add_application(app):
    applications.append(app)


def get_applications(offset=0, limit=10):
    total_count = len(applications)

    paginated_applications = applications[offset: offset + limit]

    return paginated_applications, total_count
