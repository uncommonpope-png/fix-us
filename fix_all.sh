# Fix imports and structure
find one_soul -name "*.py" | xargs sed -i 's/master_soul/one_soul.profit/g'
# Ensure templates are correctly located
mkdir -p one_soul/profit/nervous_system/templates
mv one_soul/profit/nervous_system/observatory.html one_soul/profit/nervous_system/templates/ 2>/dev/null
