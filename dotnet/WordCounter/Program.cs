using System;


namespace WordCounter
{
    class Program
    {
        static void Main(string[] args)
        {
            bool validArgument = InputArgument.IsValidArgument(args);

            if(validArgument == true)
            {
                TextFile textFile = new(args[0]);
                string contentString = textFile.FileContentToString();
                string[] contentArray = TextFile.ParseStringToArray(contentString);
                int wordCount = textFile.CountWordsInArray(contentArray);
                textFile.PrintWordCount(wordCount);
            }
        }
    }
}