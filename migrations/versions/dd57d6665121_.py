"""empty message

Revision ID: dd57d6665121
Revises: None
Create Date: 2017-02-20 13:37:22.500322

"""

# revision identifiers, used by Alembic.
revision = 'dd57d6665121'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lead_management',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('company', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=False),
    sa.Column('about_project', sa.Text(), nullable=False),
    sa.Column('project_type', sa.String(length=50), nullable=False),
    sa.Column('sign_up_news_letter', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lead_management')
    ### end Alembic commands ###
