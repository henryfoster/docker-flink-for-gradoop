from faker import Faker
import secrets
from faker.providers import DynamicProvider
from faker.providers import internet

graph = '5f4f896469518553971cdc9b'

browser_provider = DynamicProvider(
     provider_name="browser",
     elements=["Internet Explorer", "Chrome", "Mozilla Firefox", "Opera", "Edge"],
)

email_provider = DynamicProvider(
     provider_name="at_email",
     elements=["@gmail.com", "@web.de", "@hotmail.com", "@yahoo.de", "@msn.com"],
)

gender_provider = DynamicProvider(
     provider_name="gender",
     elements=["m", "w"],
)

topics_provider = DynamicProvider(
     provider_name="topics",
     elements=["sport", "music", "games", "computer", "outdoor", "indoor", "books", "movies"],
)

language_short_provider = DynamicProvider(
     provider_name="language_short",
     elements=["de", "en", "fr", "it", "ru", "pl", "es"],
)

fake = Faker()
fake.add_provider(browser_provider)
fake.add_provider(email_provider)
fake.add_provider(gender_provider)
fake.add_provider(internet)
fake.add_provider(language_short_provider)
fake.add_provider(topics_provider)



def create_person(graph):
    first_name = fake.first_name()
    last_name = fake.last_name()
    person = {
        'id': secrets.token_hex(12),
        'graph': graph,
        'label': 'person',
        'birthday': fake.date(),
        'browserUsed': fake.browser(),
        'creationDate': fake.date_time().isoformat(),
        'email': '[' + first_name + '.' + last_name + fake.at_email() + ']',
        'firstName': first_name,
        'gender': fake.gender(),
        'lastName': last_name,
        'locationIP':  fake.ipv4_public(),
        'speaks': '[' + fake.language_short() + ']'
    }
    return person


def create_post(graph, person):
    text = fake.topics()
    post = {
        'id': secrets.token_hex(12),
        'graph': graph,
        'label': 'post',
        'browserUsed': fake.browser(),
        'content': text,
        'creationDate': fake.date_time().isoformat(),
        'imageFile': secrets.token_hex(5) + 'img.jpg',
        'language': fake.language_short(),
        'length': str(len(text)),
        'locationIP': person['locationIP']
    }
    return post


def create_comment(graph, person):
    text = fake.topics()
    comment = {
        'id': secrets.token_hex(12),
        'graph': graph,
        'label': 'comment',
        'browserUsed': fake.browser(),
        'content': text,
        'creationDate': fake.date_time().isoformat(),
        'length': str(len(text)),
        'locationIP': person['locationIP']
    }
    return comment


def create_has_creator_edge(graph, message, person):
    hasCreator = {
        'id': secrets.token_hex(12),
        'graph': graph,
        'label': 'hasCreator',
        'from': message['id'],
        'to': person['id']

    }
    return hasCreator

def create_reply_of_edge(graph, comment, post):
    replyOf = {
        'id': secrets.token_hex(12),
        'graph': graph,
        'label': 'replyOf',
        'from': comment['id'],
        'to': post['id']
    }
    return replyOf

def convert_to_vertex_row(vertex):
    return f'{vertex["id"]};[{vertex["graph"]}];{vertex["label"]};{"|".join(list(vertex.values())[3:])}'

def convert_to_edge_row(edge):
    return f'{edge["id"]};[{edge["graph"]}];{edge["from"]};{edge["to"]};{edge["label"]};{"|".join(list(edge.values())[5:])}'


def generate_fake_data(graph):
    persons = []
    posts = []
    hasCreators = []
    comments = []
    replyOfs = []
    for i in range(0, 100):
        person = create_person(graph)
        persons.append(person)
        #print(convert_to_vertex_row(person))
        print(f'{str(i)}/100')
        for j in range(0, 10):
            post = create_post(graph, person)
            hasCreator = create_has_creator_edge(graph, post, person)
            comment = create_comment(graph, person)
            replyOf = create_reply_of_edge(graph, comment, post)
            hasCommentCreator = create_has_creator_edge(graph, comment, person)

            posts.append(post)
            hasCreators.append(hasCreator)
            comments.append(comment)
            replyOfs.append(replyOf)
            hasCreators.append(hasCommentCreator)

            #print(convert_to_vertex_row(post))
            #print(convert_to_edge_row(hasCreator))
            #print(convert_to_vertex_row(comment))
            #print(convert_to_edge_row(replyOf))
            #print(convert_to_edge_row(hasCommentCreator))

    with open('vertices.csv', 'w') as file:
        for line in persons:
            file.write(convert_to_vertex_row(line))
            file.write('\n')
        for line in posts:
            file.write(convert_to_vertex_row(line))
            file.write('\n')
        for line in comments:
            file.write(convert_to_vertex_row(line))
            file.write('\n')

    with open('edges.csv', 'w') as file:
        for line in hasCreators:
            file.write(convert_to_edge_row(line))
            file.write('\n')
        for line in replyOfs:
            file.write(convert_to_edge_row(line))
            file.write('\n')



def write_data_to_csv(data):
    print()


person = create_person('123')
post = create_post('123', person)
hasCreator = create_has_creator_edge('123', post, person)
#print(convert_to_edge_row(hasCreator))

generate_fake_data(graph)
