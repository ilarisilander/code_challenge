using System;


namespace WordCounter
{
    class Program
    {
        static void Main(string[] args)
        {
            bool validArgument = false;

            try
            {
                validArgument = InputArgument.IsValidArgument(args);
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }

            if(validArgument == true)
            {
                TextFile textFile = new(args[0]);
                string[] contentArray = textFile.FileContentToArray();
                int wordCount = textFile.CountWordsInArray(contentArray);
                textFile.PrintWordCount(wordCount);
            }
        }
    }
}