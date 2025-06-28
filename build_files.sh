
echo "BUILD START"
pip install -r requirement.txt

# Run Django collectstatic
python manage.py collectstatic --noinput

echo "BUILD END"