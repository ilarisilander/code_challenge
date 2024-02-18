using System;
using System.IO;


namespace WordCounter
{
    public class TextFile
    {
        public string FileName { get; set; }
        public string FilePath { get; set; }

        public TextFile(string filePath)
        {
            FilePath = filePath;
            FileName = Path.GetFileNameWithoutExtension(filePath);
        }

        public string FileContentToString()
        {
            string contentString = File.ReadAllText(FilePath, System.Text.Encoding.UTF8);
            return contentString;
        }

        public static string[] ParseStringToArray(string fileContent)
        {
            char[] separators = [' ', '\n', '\r', '\"'];
            string[] words = fileContent.Split(separators, StringSplitOptions.RemoveEmptyEntries);
            return words;
        }

        public int CountWordsInArray(string[] words)
        {
            int counter = 0;
            for(int i = 0; i < words.Length; i++)
            {
                if(words[i].Contains(FileName, StringComparison.OrdinalIgnoreCase))
                {
                    counter++;
                }
            }
            return counter;
        }

        public void PrintWordCount(int counter)
        {
            Console.WriteLine($"The word {FileName} appeared {counter} times");
        }


    }
}