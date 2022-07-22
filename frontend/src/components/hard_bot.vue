<template>
  <div class="bot">
    <p style="align-self: flex-start; font-size: 30px; margin-bottom: 0">
      Бот помощник
    </p>
    <p style="align-self: flex-start; font-size: 12px">
      Готов ответить на ваши вопросы
    </p>
    <div class="message-field">
      <el-tag
        v-for="item in all_messages"
        :key="item"
        :type="item.type"
        :class="'mess animate__animated animate__fadeIn ' + item.class"
        effect="dark"
        round
      >
        <p>{{ item.text }}</p>
      </el-tag>
    </div>

    <div class="input-field animate__animated animate__fadeIn">
      <div v-if="state === 'base'">
        <el-button
          v-for="button in buttons_base"
          :key="button.text"
          :type="button.type"
          text
          style="margin-left: 0"
          @click="base(button.text)"
          >{{ button.text }}</el-button
        >
      </div>

      <div v-if="state === 'methodic'">
        <el-button
          v-for="button in buttons_methodic"
          :key="button.text"
          :type="button.type"
          text
          style="margin-left: 0"
          @click="methodic(button.text)"
          >{{ button.text }}</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { Promotion } from "@element-plus/icons-vue";
export default {
  name: "TelegramWebApp",
  data() {
    return {
      Promotion: Promotion,
      input_text: "",
      state: "base",
      all_messages: [],
      buttons_base: [
        { type: "warning", text: "Информация о методике" },
        { type: "warning", text: "О нас" },
        { type: "warning", text: "Контакты" },
        { type: "warning", text: "Стоимость" },
        { type: "warning", text: "Условия выполнения" },
      ],
      buttons_methodic: [
        { type: "warning", text: "Хочу записаться" },
        { type: "warning", text: "Подхожу ли я данной методике?" },
        { type: "warning", text: "Что из себя представляет эта методика?" },
        { type: "warning", text: "Стоит ли мне проходить методику?" },
        { type: "warning", text: "← Назад" },
      ],
    };
  },
  methods: {
    base(text) {
      this.mes_user(text);
      switch (text) {
        case "Информация о методике":
          this.mes_bot("Что вы хотите узнать?");
          this.state = "methodic";
          break;
        default:
          console.log("Error");
      }
    },

    methodic(text) {
      this.mes_user(text);
      switch (text) {
        case "Хочу записаться":
          this.mes_bot("Какой-то заготовленный текст");
          this.state = "methodic";
          break;
        case "Подхожу ли я данной методике?":
          this.mes_bot("Какой-то заготовленный текст");
          this.state = "methodic";
          break;
        case "Что из себя представляет эта методика?":
          this.mes_bot("Какой-то заготовленный текст");
          this.state = "methodic";
          break;
        case "Стоит ли мне проходить методику?":
          this.mes_bot("Какой-то заготовленный текст");
          this.state = "methodic";
          break;
        default:
          this.mes_bot("Главное меню");
          this.state = "base";
      }
    },

    mes_user(text) {
      setTimeout(() => {
        this.all_messages = [
          {
            text: text,
            class: "mes-user",
            type: "success",
          },
        ].concat(this.all_messages);
      }, 500);
    },

    mes_bot(text) {
      setTimeout(() => {
        this.all_messages = [
          {
            text: text,
            class: "mes-bot",
            type: "",
          },
        ].concat(this.all_messages);
      }, 500);
    },
  },
  mounted() {
    setTimeout(() => {
      this.all_messages = [
        {
          text: "Здравствуйте",
          class: "mes-bot",
          type: "",
        },
      ].concat(this.all_messages);

      setTimeout(() => {
        this.all_messages = [
          {
            text: "Выберите любой интерисующий вас вопрос - и я с удовольствием на него отвечу",
            class: "mes-bot",
            type: "",
          },
        ].concat(this.all_messages);

        setTimeout(() => {
          this.all_messages = [
            {
              text: "Выберите тематику вопроса:",
              class: "mes-bot",
              type: "",
            },
          ].concat(this.all_messages);
        }, 500);
      }, 500);
    }, 500);
  },
};
</script>

<style lang="scss">
.bot {
  width: 100%;
  display: flex;
  flex-direction: column;

  .message-field {
    height: 50vh;
    display: flex;
    flex-direction: column-reverse;
    align-items: flex-end;
    margin-bottom: 10px;

    .mess {
      height: 40px;

      p {
        margin-bottom: 0;
        margin: 2px;
        white-space: normal;
      }
    }

    .mes-user {
      align-self: flex-end;
      margin: 13px;
    }

    .mes-bot {
      align-self: flex-start;
      margin: 5px;
    }
  }

  .input-field {
    justify-content: center;
    align-items: center;
    width: 100%;
  }
}
</style>
