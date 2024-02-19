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
            catch(ArgumentException ae)
            {
                Console.WriteLine($"Error: {ae.Message}");
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }

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