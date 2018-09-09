WORKING_DIR=$(pwd)
ZIPFILE="deployment-package.zip"
LAMBDA_HANDLER="lambda_function.py"
FUNCTION_NAME="iOSRestrictionPasscodeBruteForce"

echo "Cleaning .DS_Store's"
find . -name '.DS_Store' -type f -delete

echo "Creating $ZIPFILE..."
rm "$ZIPFILE"
zip -rq "$ZIPFILE" "passlib"
zip -uq "$ZIPFILE" "$LAMBDA_HANDLER"
echo "Created $ZIPFILE"

echo "Uploading $ZIPFILE..."
aws lambda update-function-code --function-name "$FUNCTION_NAME" --zip-file fileb://"$ZIPFILE" >> deploy.log & UPDATE_PID=$!

printf "["
while kill -0 $UPDATE_PID 2> /dev/null; do
    printf  "▓"
    sleep 0.25
done
printf "]"

echo "Uploaded $ZIPFILE"
echo "Successfully updated $FUNCTION_NAME"
