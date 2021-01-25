import psycopg2
import os
import pandas as pd


def format_queue(row: pd.Series):
    '''
    Format a queue using HTML as a li element and add to the series.
    :param row: pd.Series representing one unique queue-host combination.
    :return: pd.Series with new column 'formatted'.
    '''
    queue_name = row['queue_name']
    settings_link = row['settings_link']
    settings_link_ahref = f'<a href="{settings_link}">{settings_link}</a>'
    row['formatted'] = f'<li>{queue_name}: {settings_link_ahref}</li>'
    return row


conn = psycopg2.connect(
    host=os.getenv('host'),
    port=5432,
    database='officehours',
    user=os.getenv('user'),
    password=os.getenv('password')
)

host_query = '''select 
                    au.first_name,
                    au.last_name,
                    au.username,
                    au.email,
                    au.last_login,
                    q."name" as "queue_name",
                    q.allowed_backends,
                    concat('https://officehours.it.umich.edu/manage/',q.id,'/settings') as "settings_link"
                from officehours_api_queue_hosts qh
                full outer join auth_user au ON qh.user_id = au.id
                right join officehours_api_queue q on q.id = qh.queue_id 
                where 
                    q.deleted is null and 
                    q.allowed_backends @> array['bluejeans']::varchar[];'''

df = pd.read_sql(host_query, conn)  # Get queues with BlueJeans enabled
conn.close()

df = df.apply(format_queue, axis=1)  # Format each queue individually
grouped = df.groupby(['email'])['formatted'].apply(' '.join).reset_index()  # Join all of a host's queues using a space
grouped['queues_html'] = grouped['formatted'].apply(lambda x: f'<ul>{x}</ul>')  # Encase in ul tag
grouped = grouped[['email', 'queues_html']]  # Drop 'formatted' column, no longer needed
grouped.to_csv('hosts_bluejeans.csv', index=False)
